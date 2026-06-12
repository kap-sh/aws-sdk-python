"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexVideoSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min100000_max100000000
    import aws_sdk_medialive.types.multiplex_statmux_video_settings


class MultiplexVideoSettings(TypedDict):
    constant_bitrate: NotRequired[
        "aws_sdk_medialive.types.__integer_min100000_max100000000.__integerMin100000Max100000000"
    ]
    """The constant bitrate configuration for the video encode. When this field is defined, StatmuxSettings must be undefined."""
    statmux_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_statmux_video_settings.MultiplexStatmuxVideoSettings"
    ]
    """Statmux rate control settings. When this field is defined, ConstantBitrate must be undefined."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexVideoSettings) -> dict:
    out: dict = {}
    if "constant_bitrate" in value:
        out["constantBitrate"] = value["constant_bitrate"]
    if "statmux_settings" in value:
        import aws_sdk_medialive.types.multiplex_statmux_video_settings

        out["statmuxSettings"] = (
            aws_sdk_medialive.types.multiplex_statmux_video_settings.serialize_json(
                value["statmux_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexVideoSettings:
    out: MultiplexVideoSettings = {}  # type: ignore[typeddict-item]
    if "constantBitrate" in data:
        out["constant_bitrate"] = data["constantBitrate"]
    if "statmuxSettings" in data:
        import aws_sdk_medialive.types.multiplex_statmux_video_settings

        out["statmux_settings"] = (
            aws_sdk_medialive.types.multiplex_statmux_video_settings.deserialize_json(
                data["statmuxSettings"]
            )
        )
    return out
