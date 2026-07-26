"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ViewSunAzimuthInput``."""

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError


class ViewSunAzimuthInput(TypedDict, closed=True):
    lower_bound: "float"
    """<p>The minimum value for ViewSunAzimuth property filter. This filters items having ViewSunAzimuth greater than or equal to this value.</p>"""
    upper_bound: "float"
    """<p>The maximum value for ViewSunAzimuth property filter. This filters items having ViewSunAzimuth lesser than or equal to this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewSunAzimuthInput) -> dict:
    out: dict = {}
    out["LowerBound"] = value["lower_bound"]
    out["UpperBound"] = value["upper_bound"]
    return out


def deserialize_json(data: dict) -> ViewSunAzimuthInput:
    out: ViewSunAzimuthInput = {}  # type: ignore[typeddict-item]
    if "LowerBound" in data:
        out["lower_bound"] = data["LowerBound"]
    else:
        raise DeserializationError("ViewSunAzimuthInput.lower_bound required")
    if "UpperBound" in data:
        out["upper_bound"] = data["UpperBound"]
    else:
        raise DeserializationError("ViewSunAzimuthInput.upper_bound required")
    return out
