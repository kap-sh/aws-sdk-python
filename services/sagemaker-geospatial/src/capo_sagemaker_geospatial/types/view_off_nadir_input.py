"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ViewOffNadirInput``."""

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError


class ViewOffNadirInput(TypedDict, closed=True):
    lower_bound: "float"
    """<p>The minimum value for ViewOffNadir property filter. This filters items having ViewOffNadir greater than or equal to this value. </p>"""
    upper_bound: "float"
    """<p>The maximum value for ViewOffNadir property filter. This filters items having ViewOffNadir lesser than or equal to this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewOffNadirInput) -> dict:
    out: dict = {}
    out["LowerBound"] = value["lower_bound"]
    out["UpperBound"] = value["upper_bound"]
    return out


def deserialize_json(data: dict) -> ViewOffNadirInput:
    out: ViewOffNadirInput = {}  # type: ignore[typeddict-item]
    if "LowerBound" in data:
        out["lower_bound"] = data["LowerBound"]
    else:
        raise DeserializationError("ViewOffNadirInput.lower_bound required")
    if "UpperBound" in data:
        out["upper_bound"] = data["UpperBound"]
    else:
        raise DeserializationError("ViewOffNadirInput.upper_bound required")
    return out
