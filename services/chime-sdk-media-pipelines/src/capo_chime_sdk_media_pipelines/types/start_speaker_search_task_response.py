"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#StartSpeakerSearchTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.speaker_search_task


class StartSpeakerSearchTaskResponse(TypedDict, closed=True):
    speaker_search_task: NotRequired[
        "capo_chime_sdk_media_pipelines.types.speaker_search_task.SpeakerSearchTask"
    ]
    """<p>The details of the speaker search task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeakerSearchTaskResponse) -> dict:
    out: dict = {}
    if "speaker_search_task" in value:
        import capo_chime_sdk_media_pipelines.types.speaker_search_task

        out["SpeakerSearchTask"] = (
            capo_chime_sdk_media_pipelines.types.speaker_search_task.serialize_json(
                value["speaker_search_task"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartSpeakerSearchTaskResponse:
    out: StartSpeakerSearchTaskResponse = {}  # type: ignore[typeddict-item]
    if "SpeakerSearchTask" in data:
        import capo_chime_sdk_media_pipelines.types.speaker_search_task

        out["speaker_search_task"] = (
            capo_chime_sdk_media_pipelines.types.speaker_search_task.deserialize_json(
                data["SpeakerSearchTask"]
            )
        )
    return out
