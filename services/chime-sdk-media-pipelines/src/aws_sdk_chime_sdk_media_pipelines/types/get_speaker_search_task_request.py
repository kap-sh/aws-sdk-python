"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetSpeakerSearchTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.guid_string
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string


class GetSpeakerSearchTaskRequest(TypedDict, closed=True):
    identifier: (
        "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>"""
    speaker_search_task_id: (
        "aws_sdk_chime_sdk_media_pipelines.types.guid_string.GuidString"
    )
    """<p>The ID of the speaker search task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpeakerSearchTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSpeakerSearchTaskRequest:
    out: GetSpeakerSearchTaskRequest = {}  # type: ignore[typeddict-item]
    return out
