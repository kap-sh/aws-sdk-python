"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#DeleteMediaPipelineKinesisVideoStreamPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.non_empty_string


class DeleteMediaPipelineKinesisVideoStreamPoolRequest(TypedDict, closed=True):
    identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier of the requested resource. Valid values include the name and ARN of the media pipeline Kinesis Video Stream pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMediaPipelineKinesisVideoStreamPoolRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMediaPipelineKinesisVideoStreamPoolRequest:
    out: DeleteMediaPipelineKinesisVideoStreamPoolRequest = {}  # type: ignore[typeddict-item]
    return out
