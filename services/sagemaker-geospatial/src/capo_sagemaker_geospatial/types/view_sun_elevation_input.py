"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ViewSunElevationInput``."""

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError


class ViewSunElevationInput(TypedDict, closed=True):
    lower_bound: "float"
    """<p>The lower bound to view the sun elevation.</p>"""
    upper_bound: "float"
    """<p>The upper bound to view the sun elevation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewSunElevationInput) -> dict:
    out: dict = {}
    out["LowerBound"] = value["lower_bound"]
    out["UpperBound"] = value["upper_bound"]
    return out


def deserialize_json(data: dict) -> ViewSunElevationInput:
    out: ViewSunElevationInput = {}  # type: ignore[typeddict-item]
    if "LowerBound" in data:
        out["lower_bound"] = data["LowerBound"]
    else:
        raise DeserializationError("ViewSunElevationInput.lower_bound required")
    if "UpperBound" in data:
        out["upper_bound"] = data["UpperBound"]
    else:
        raise DeserializationError("ViewSunElevationInput.upper_bound required")
    return out
