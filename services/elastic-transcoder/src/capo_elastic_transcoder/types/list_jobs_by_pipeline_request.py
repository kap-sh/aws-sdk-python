"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ListJobsByPipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.ascending
    import capo_elastic_transcoder.types.id


class ListJobsByPipelineRequest(TypedDict, closed=True):
    pipeline_id: "capo_elastic_transcoder.types.id.Id"
    """<p>The ID of the pipeline for which you want to get job information.</p>"""
    ascending: NotRequired["capo_elastic_transcoder.types.ascending.Ascending"]
    """<p> To list jobs in chronological order by the date and time that they were submitted, enter <code>true</code>. To list jobs in reverse chronological order, enter <code>false</code>. </p>"""
    page_token: NotRequired["capo_elastic_transcoder.types.id.Id"]
    """<p> When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobsByPipelineRequest:
    out: ListJobsByPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
