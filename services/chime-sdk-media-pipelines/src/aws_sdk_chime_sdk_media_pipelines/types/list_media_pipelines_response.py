"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ListMediaPipelinesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_list
    import aws_sdk_chime_sdk_media_pipelines.types.string


class ListMediaPipelinesResponse(TypedDict, closed=True):
    media_pipelines: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_list.MediaPipelineList"
    ]
    """<p>The media pipeline objects in the list.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.string.String"]
    """<p>The token used to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMediaPipelinesResponse) -> dict:
    out: dict = {}
    if "media_pipelines" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_list

        out["MediaPipelines"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_list.serialize_json(
                value["media_pipelines"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMediaPipelinesResponse:
    out: ListMediaPipelinesResponse = {}  # type: ignore[typeddict-item]
    if "MediaPipelines" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_list

        out["media_pipelines"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_list.deserialize_json(
                data["MediaPipelines"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
