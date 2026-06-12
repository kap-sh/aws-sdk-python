"""Generated from Smithy shape ``com.amazonaws.medialive#StopTimecode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.last_frame_clipping_behavior


class StopTimecode(TypedDict):
    last_frame_clipping_behavior: NotRequired[
        "aws_sdk_medialive.types.last_frame_clipping_behavior.LastFrameClippingBehavior"
    ]
    """If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode."""
    timecode: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF."""


# --- restJson1 ser/de ---
def serialize_json(value: StopTimecode) -> dict:
    out: dict = {}
    if "last_frame_clipping_behavior" in value:
        import aws_sdk_medialive.types.last_frame_clipping_behavior

        out["lastFrameClippingBehavior"] = (
            aws_sdk_medialive.types.last_frame_clipping_behavior.serialize_json(
                value["last_frame_clipping_behavior"]
            )
        )
    if "timecode" in value:
        out["timecode"] = value["timecode"]
    return out


def deserialize_json(data: dict) -> StopTimecode:
    out: StopTimecode = {}  # type: ignore[typeddict-item]
    if "lastFrameClippingBehavior" in data:
        import aws_sdk_medialive.types.last_frame_clipping_behavior

        out["last_frame_clipping_behavior"] = (
            aws_sdk_medialive.types.last_frame_clipping_behavior.deserialize_json(
                data["lastFrameClippingBehavior"]
            )
        )
    if "timecode" in data:
        out["timecode"] = data["timecode"]
    return out
