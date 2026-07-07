"""Generated from Smithy shape ``com.amazonaws.medialive#InputChannelLevel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0_max15
    import aws_sdk_medialive.types.__integer_min_negative60_max6


class InputChannelLevel(TypedDict, closed=True):
    gain: NotRequired[
        "aws_sdk_medialive.types.__integer_min_negative60_max6.__integerMinNegative60Max6"
    ]
    """Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB."""
    input_channel: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max15.__integerMin0Max15"
    ]
    """The index of the input channel used as a source."""


# --- restJson1 ser/de ---
def serialize_json(value: InputChannelLevel) -> dict:
    out: dict = {}
    if "gain" in value:
        out["gain"] = value["gain"]
    if "input_channel" in value:
        out["inputChannel"] = value["input_channel"]
    return out


def deserialize_json(data: dict) -> InputChannelLevel:
    out: InputChannelLevel = {}  # type: ignore[typeddict-item]
    if "gain" in data:
        out["gain"] = data["gain"]
    if "inputChannel" in data:
        out["input_channel"] = data["inputChannel"]
    return out
