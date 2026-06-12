"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseReducerFilterSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max3


class NoiseReducerFilterSettings(TypedDict):
    strength: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max3.__integerMin0Max3"
    ]
    """Relative strength of noise reducing filter. Higher values produce stronger filtering."""


# --- restJson1 ser/de ---
def serialize_json(value: NoiseReducerFilterSettings) -> dict:
    out: dict = {}
    if "strength" in value:
        out["strength"] = value["strength"]
    return out


def deserialize_json(data: dict) -> NoiseReducerFilterSettings:
    out: NoiseReducerFilterSettings = {}  # type: ignore[typeddict-item]
    if "strength" in data:
        out["strength"] = data["strength"]
    return out
