"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#LandsatCloudCoverLandInput``."""

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError


class LandsatCloudCoverLandInput(TypedDict, closed=True):
    lower_bound: "float"
    """<p>The minimum value for Land Cloud Cover property filter. This will filter items having Land Cloud Cover greater than or equal to this value.</p>"""
    upper_bound: "float"
    """<p>The maximum value for Land Cloud Cover property filter. This will filter items having Land Cloud Cover less than or equal to this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandsatCloudCoverLandInput) -> dict:
    out: dict = {}
    out["LowerBound"] = value["lower_bound"]
    out["UpperBound"] = value["upper_bound"]
    return out


def deserialize_json(data: dict) -> LandsatCloudCoverLandInput:
    out: LandsatCloudCoverLandInput = {}  # type: ignore[typeddict-item]
    if "LowerBound" in data:
        out["lower_bound"] = data["LowerBound"]
    else:
        raise DeserializationError("LandsatCloudCoverLandInput.lower_bound required")
    if "UpperBound" in data:
        out["upper_bound"] = data["UpperBound"]
    else:
        raise DeserializationError("LandsatCloudCoverLandInput.upper_bound required")
    return out
