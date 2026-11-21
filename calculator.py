"""Core calculation for the exploratory 30-day PE combined-endpoint model."""
from math import exp

INTERCEPT = -2.9908061853634647
COEFFICIENTS = {
    "low_hb": 1.604313608706529,
    "atrial_fibrillation": 1.3918853652584597,
    "immobilization_4_weeks": 1.218753367733765,
    "tapse_below_16": 1.2275903731972855,
}


def calculate_probability(
    low_hb: bool,
    atrial_fibrillation: bool,
    immobilization_4_weeks: bool,
    tapse_below_16: bool,
) -> dict:
    """Return linear predictor z and probability on the 0-1 scale."""
    values = {
        "low_hb": int(bool(low_hb)),
        "atrial_fibrillation": int(bool(atrial_fibrillation)),
        "immobilization_4_weeks": int(bool(immobilization_4_weeks)),
        "tapse_below_16": int(bool(tapse_below_16)),
    }
    z = INTERCEPT + sum(COEFFICIENTS[key] * value for key, value in values.items())
    # Numerically stable logistic transform
    if z >= 0:
        probability = 1.0 / (1.0 + exp(-z))
    else:
        ez = exp(z)
        probability = ez / (1.0 + ez)
    return {"z": z, "probability": probability, "probability_percent": probability * 100,
            "predictor_count": sum(values.values()), "inputs": values}
