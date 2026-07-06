"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#UpdateMediaInsightsPipelineStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status_update
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string


class UpdateMediaInsightsPipelineStatusRequest(TypedDict, closed=True):
    identifier: (
        "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>"""
    update_status: "aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status_update.MediaPipelineStatusUpdate"
    """<p>The requested status of the media insights pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMediaInsightsPipelineStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status_update

    out["UpdateStatus"] = (
        aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status_update.serialize_json(
            value["update_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateMediaInsightsPipelineStatusRequest:
    out: UpdateMediaInsightsPipelineStatusRequest = {}  # type: ignore[typeddict-item]
    if "UpdateStatus" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status_update

        out["update_status"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status_update.deserialize_json(
                data["UpdateStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateMediaInsightsPipelineStatusRequest.update_status required"
        )
    return out
