"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SccDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.scc_destination_framerate


class SccDestinationSettings(TypedDict, closed=True):
    framerate: NotRequired[
        "aws_sdk_mediaconvert.types.scc_destination_framerate.SccDestinationFramerate"
    ]
    """Set Framerate to make sure that the captions and the video are synchronized in the output. Specify a frame rate that matches the frame rate of the associated video. If the video frame rate is 29.97, choose 29.97 dropframe only if the video has video_insertion=true and drop_frame_timecode=true; otherwise, choose 29.97 non-dropframe."""


# --- restJson1 ser/de ---
def serialize_json(value: SccDestinationSettings) -> dict:
    out: dict = {}
    if "framerate" in value:
        import aws_sdk_mediaconvert.types.scc_destination_framerate

        out["framerate"] = (
            aws_sdk_mediaconvert.types.scc_destination_framerate.serialize_json(
                value["framerate"]
            )
        )
    return out


def deserialize_json(data: dict) -> SccDestinationSettings:
    out: SccDestinationSettings = {}  # type: ignore[typeddict-item]
    if "framerate" in data:
        import aws_sdk_mediaconvert.types.scc_destination_framerate

        out["framerate"] = (
            aws_sdk_mediaconvert.types.scc_destination_framerate.deserialize_json(
                data["framerate"]
            )
        )
    return out
