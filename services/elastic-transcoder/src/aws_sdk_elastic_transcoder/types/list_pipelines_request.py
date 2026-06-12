"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ListPipelinesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.ascending
    import aws_sdk_elastic_transcoder.types.id


class ListPipelinesRequest(TypedDict):
    ascending: NotRequired["aws_sdk_elastic_transcoder.types.ascending.Ascending"]
    """<p>To list pipelines in chronological order by the date and time that they were created, enter <code>true</code>. To list pipelines in reverse chronological order, enter <code>false</code>.</p>"""
    page_token: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p>When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelinesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPipelinesRequest:
    out: ListPipelinesRequest = {}  # type: ignore[typeddict-item]
    return out
