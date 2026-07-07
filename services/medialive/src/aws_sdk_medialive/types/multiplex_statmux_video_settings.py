"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexStatmuxVideoSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min100000_max100000000
    import aws_sdk_medialive.types.__integer_min_negative5_max5


class MultiplexStatmuxVideoSettings(TypedDict, closed=True):
    maximum_bitrate: NotRequired[
        "aws_sdk_medialive.types.__integer_min100000_max100000000.__integerMin100000Max100000000"
    ]
    """Maximum statmux bitrate."""
    minimum_bitrate: NotRequired[
        "aws_sdk_medialive.types.__integer_min100000_max100000000.__integerMin100000Max100000000"
    ]
    """Minimum statmux bitrate."""
    priority: NotRequired[
        "aws_sdk_medialive.types.__integer_min_negative5_max5.__integerMinNegative5Max5"
    ]
    r"""The purpose of the priority is to use a combination of the\nmultiplex rate control algorithm and the QVBR capability of the\nencoder to prioritize the video quality of some channels in a\nmultiplex over others. Channels that have a higher priority will\nget higher video quality at the expense of the video quality of\nother channels in the multiplex with lower priority."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexStatmuxVideoSettings) -> dict:
    out: dict = {}
    if "maximum_bitrate" in value:
        out["maximumBitrate"] = value["maximum_bitrate"]
    if "minimum_bitrate" in value:
        out["minimumBitrate"] = value["minimum_bitrate"]
    if "priority" in value:
        out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> MultiplexStatmuxVideoSettings:
    out: MultiplexStatmuxVideoSettings = {}  # type: ignore[typeddict-item]
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    if "minimumBitrate" in data:
        out["minimum_bitrate"] = data["minimumBitrate"]
    if "priority" in data:
        out["priority"] = data["priority"]
    return out
