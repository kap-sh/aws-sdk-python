"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ListMediaCapturePipelinesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_capture_pipeline_summary_list
    import capo_chime_sdk_media_pipelines.types.string


class ListMediaCapturePipelinesResponse(TypedDict, closed=True):
    media_capture_pipelines: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_capture_pipeline_summary_list.MediaCapturePipelineSummaryList"
    ]
    """<p>The media pipeline objects in the list.</p>"""
    next_token: NotRequired["capo_chime_sdk_media_pipelines.types.string.String"]
    """<p>The token used to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMediaCapturePipelinesResponse) -> dict:
    out: dict = {}
    if "media_capture_pipelines" in value:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline_summary_list

        out["MediaCapturePipelines"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline_summary_list.serialize_json(
                value["media_capture_pipelines"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMediaCapturePipelinesResponse:
    out: ListMediaCapturePipelinesResponse = {}  # type: ignore[typeddict-item]
    if "MediaCapturePipelines" in data:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline_summary_list

        out["media_capture_pipelines"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline_summary_list.deserialize_json(
                data["MediaCapturePipelines"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
