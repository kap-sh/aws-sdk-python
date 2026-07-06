"""Generated from Smithy shape ``com.amazonaws.medialive#InputClippingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_timecode_source
    import aws_sdk_medialive.types.start_timecode
    import aws_sdk_medialive.types.stop_timecode


class InputClippingSettings(TypedDict, closed=True):
    input_timecode_source: NotRequired[
        "aws_sdk_medialive.types.input_timecode_source.InputTimecodeSource"
    ]
    """The source of the timecodes in the source being clipped."""
    start_timecode: NotRequired["aws_sdk_medialive.types.start_timecode.StartTimecode"]
    """Settings to identify the start of the clip."""
    stop_timecode: NotRequired["aws_sdk_medialive.types.stop_timecode.StopTimecode"]
    """Settings to identify the end of the clip."""


# --- restJson1 ser/de ---
def serialize_json(value: InputClippingSettings) -> dict:
    out: dict = {}
    if "input_timecode_source" in value:
        import aws_sdk_medialive.types.input_timecode_source

        out["inputTimecodeSource"] = (
            aws_sdk_medialive.types.input_timecode_source.serialize_json(
                value["input_timecode_source"]
            )
        )
    if "start_timecode" in value:
        import aws_sdk_medialive.types.start_timecode

        out["startTimecode"] = aws_sdk_medialive.types.start_timecode.serialize_json(
            value["start_timecode"]
        )
    if "stop_timecode" in value:
        import aws_sdk_medialive.types.stop_timecode

        out["stopTimecode"] = aws_sdk_medialive.types.stop_timecode.serialize_json(
            value["stop_timecode"]
        )
    return out


def deserialize_json(data: dict) -> InputClippingSettings:
    out: InputClippingSettings = {}  # type: ignore[typeddict-item]
    if "inputTimecodeSource" in data:
        import aws_sdk_medialive.types.input_timecode_source

        out["input_timecode_source"] = (
            aws_sdk_medialive.types.input_timecode_source.deserialize_json(
                data["inputTimecodeSource"]
            )
        )
    if "startTimecode" in data:
        import aws_sdk_medialive.types.start_timecode

        out["start_timecode"] = aws_sdk_medialive.types.start_timecode.deserialize_json(
            data["startTimecode"]
        )
    if "stopTimecode" in data:
        import aws_sdk_medialive.types.stop_timecode

        out["stop_timecode"] = aws_sdk_medialive.types.stop_timecode.deserialize_json(
            data["stopTimecode"]
        )
    return out
