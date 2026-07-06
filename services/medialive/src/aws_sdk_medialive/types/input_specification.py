"""Generated from Smithy shape ``com.amazonaws.medialive#InputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_codec
    import aws_sdk_medialive.types.input_maximum_bitrate
    import aws_sdk_medialive.types.input_resolution


class InputSpecification(TypedDict, closed=True):
    codec: NotRequired["aws_sdk_medialive.types.input_codec.InputCodec"]
    """Input codec"""
    maximum_bitrate: NotRequired[
        "aws_sdk_medialive.types.input_maximum_bitrate.InputMaximumBitrate"
    ]
    """Maximum input bitrate, categorized coarsely"""
    resolution: NotRequired["aws_sdk_medialive.types.input_resolution.InputResolution"]
    """Input resolution, categorized coarsely"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSpecification) -> dict:
    out: dict = {}
    if "codec" in value:
        import aws_sdk_medialive.types.input_codec

        out["codec"] = aws_sdk_medialive.types.input_codec.serialize_json(
            value["codec"]
        )
    if "maximum_bitrate" in value:
        import aws_sdk_medialive.types.input_maximum_bitrate

        out["maximumBitrate"] = (
            aws_sdk_medialive.types.input_maximum_bitrate.serialize_json(
                value["maximum_bitrate"]
            )
        )
    if "resolution" in value:
        import aws_sdk_medialive.types.input_resolution

        out["resolution"] = aws_sdk_medialive.types.input_resolution.serialize_json(
            value["resolution"]
        )
    return out


def deserialize_json(data: dict) -> InputSpecification:
    out: InputSpecification = {}  # type: ignore[typeddict-item]
    if "codec" in data:
        import aws_sdk_medialive.types.input_codec

        out["codec"] = aws_sdk_medialive.types.input_codec.deserialize_json(
            data["codec"]
        )
    if "maximumBitrate" in data:
        import aws_sdk_medialive.types.input_maximum_bitrate

        out["maximum_bitrate"] = (
            aws_sdk_medialive.types.input_maximum_bitrate.deserialize_json(
                data["maximumBitrate"]
            )
        )
    if "resolution" in data:
        import aws_sdk_medialive.types.input_resolution

        out["resolution"] = aws_sdk_medialive.types.input_resolution.deserialize_json(
            data["resolution"]
        )
    return out
