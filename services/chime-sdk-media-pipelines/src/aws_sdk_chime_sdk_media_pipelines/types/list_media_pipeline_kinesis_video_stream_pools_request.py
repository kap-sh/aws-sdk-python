"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ListMediaPipelineKinesisVideoStreamPoolsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.result_max
    import aws_sdk_chime_sdk_media_pipelines.types.string


class ListMediaPipelineKinesisVideoStreamPoolsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.string.String"]
    """<p>The token used to return the next page of results. </p>"""
    max_results: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.result_max.ResultMax"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMediaPipelineKinesisVideoStreamPoolsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMediaPipelineKinesisVideoStreamPoolsRequest:
    out: ListMediaPipelineKinesisVideoStreamPoolsRequest = {}  # type: ignore[typeddict-item]
    return out
