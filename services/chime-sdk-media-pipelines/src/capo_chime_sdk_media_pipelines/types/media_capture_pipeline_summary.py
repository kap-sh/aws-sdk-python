"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaCapturePipelineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.amazon_resource_name
    import capo_chime_sdk_media_pipelines.types.guid_string


class MediaCapturePipelineSummary(TypedDict, closed=True):
    media_pipeline_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of the media pipeline in the summary.</p>"""
    media_pipeline_arn: NotRequired[
        "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the media pipeline in the summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaCapturePipelineSummary) -> dict:
    out: dict = {}
    if "media_pipeline_id" in value:
        out["MediaPipelineId"] = value["media_pipeline_id"]
    if "media_pipeline_arn" in value:
        out["MediaPipelineArn"] = value["media_pipeline_arn"]
    return out


def deserialize_json(data: dict) -> MediaCapturePipelineSummary:
    out: MediaCapturePipelineSummary = {}  # type: ignore[typeddict-item]
    if "MediaPipelineId" in data:
        out["media_pipeline_id"] = data["MediaPipelineId"]
    if "MediaPipelineArn" in data:
        out["media_pipeline_arn"] = data["MediaPipelineArn"]
    return out
