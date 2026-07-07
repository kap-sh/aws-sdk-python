"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaPipelineKinesisVideoStreamPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string


class GetMediaPipelineKinesisVideoStreamPoolRequest(TypedDict, closed=True):
    identifier: (
        "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the requested resource. Valid values include the name and ARN of the media pipeline Kinesis Video Stream pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaPipelineKinesisVideoStreamPoolRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMediaPipelineKinesisVideoStreamPoolRequest:
    out: GetMediaPipelineKinesisVideoStreamPoolRequest = {}  # type: ignore[typeddict-item]
    return out
