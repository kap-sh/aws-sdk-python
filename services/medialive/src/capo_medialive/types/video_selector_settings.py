"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.video_selector_pid
    import capo_medialive.types.video_selector_program_id


class VideoSelectorSettings(TypedDict, closed=True):
    video_selector_pid: NotRequired[
        "capo_medialive.types.video_selector_pid.VideoSelectorPid"
    ]
    video_selector_program_id: NotRequired[
        "capo_medialive.types.video_selector_program_id.VideoSelectorProgramId"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelectorSettings) -> dict:
    out: dict = {}
    if "video_selector_pid" in value:
        import capo_medialive.types.video_selector_pid

        out["videoSelectorPid"] = (
            capo_medialive.types.video_selector_pid.serialize_json(
                value["video_selector_pid"]
            )
        )
    if "video_selector_program_id" in value:
        import capo_medialive.types.video_selector_program_id

        out["videoSelectorProgramId"] = (
            capo_medialive.types.video_selector_program_id.serialize_json(
                value["video_selector_program_id"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoSelectorSettings:
    out: VideoSelectorSettings = {}  # type: ignore[typeddict-item]
    if "videoSelectorPid" in data:
        import capo_medialive.types.video_selector_pid

        out["video_selector_pid"] = (
            capo_medialive.types.video_selector_pid.deserialize_json(
                data["videoSelectorPid"]
            )
        )
    if "videoSelectorProgramId" in data:
        import capo_medialive.types.video_selector_program_id

        out["video_selector_program_id"] = (
            capo_medialive.types.video_selector_program_id.deserialize_json(
                data["videoSelectorProgramId"]
            )
        )
    return out
