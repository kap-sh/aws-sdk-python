"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#EoCloudCoverInput``."""

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError


class EoCloudCoverInput(TypedDict, closed=True):
    lower_bound: "float"
    """<p>Lower bound for EoCloudCover.</p>"""
    upper_bound: "float"
    """<p>Upper bound for EoCloudCover.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EoCloudCoverInput) -> dict:
    out: dict = {}
    out["LowerBound"] = value["lower_bound"]
    out["UpperBound"] = value["upper_bound"]
    return out


def deserialize_json(data: dict) -> EoCloudCoverInput:
    out: EoCloudCoverInput = {}  # type: ignore[typeddict-item]
    if "LowerBound" in data:
        out["lower_bound"] = data["LowerBound"]
    else:
        raise DeserializationError("EoCloudCoverInput.lower_bound required")
    if "UpperBound" in data:
        out["upper_bound"] = data["UpperBound"]
    else:
        raise DeserializationError("EoCloudCoverInput.upper_bound required")
    return out
