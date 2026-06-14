"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TimecodeBurnin``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min10_max48
    import aws_sdk_mediaconvert.types.__string_pattern
    import aws_sdk_mediaconvert.types.timecode_burnin_position


class TimecodeBurnin(TypedDict):
    font_size: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min10_max48.__integerMin10Max48"
    ]
    """Use Font size to set the font size of any burned-in timecode. Valid values are 10, 16, 32, 48."""
    position: NotRequired[
        "aws_sdk_mediaconvert.types.timecode_burnin_position.TimecodeBurninPosition"
    ]
    """Use Position under Timecode burn-in to specify the location the burned-in timecode on output video."""
    prefix: NotRequired["aws_sdk_mediaconvert.types.__string_pattern.__stringPattern"]
    r"""Use Prefix to place ASCII characters before any burned-in timecode. For example, a prefix of \"EZ-\" will result in the timecode \"EZ-00:00:00:00\". Provide either the characters themselves or the ASCII code equivalents. The supported range of characters is 0x20 through 0x7e. This includes letters, numbers, and all special characters represented on a standard English keyboard."""


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeBurnin) -> dict:
    out: dict = {}
    if "font_size" in value:
        out["fontSize"] = value["font_size"]
    if "position" in value:
        import aws_sdk_mediaconvert.types.timecode_burnin_position

        out["position"] = (
            aws_sdk_mediaconvert.types.timecode_burnin_position.serialize_json(
                value["position"]
            )
        )
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> TimecodeBurnin:
    out: TimecodeBurnin = {}  # type: ignore[typeddict-item]
    if "fontSize" in data:
        out["font_size"] = data["fontSize"]
    if "position" in data:
        import aws_sdk_mediaconvert.types.timecode_burnin_position

        out["position"] = (
            aws_sdk_mediaconvert.types.timecode_burnin_position.deserialize_json(
                data["position"]
            )
        )
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
