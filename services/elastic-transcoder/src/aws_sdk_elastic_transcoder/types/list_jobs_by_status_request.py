"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ListJobsByStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.ascending
    import aws_sdk_elastic_transcoder.types.id
    import aws_sdk_elastic_transcoder.types.job_status


class ListJobsByStatusRequest(TypedDict, closed=True):
    status: "aws_sdk_elastic_transcoder.types.job_status.JobStatus"
    """<p>To get information about all of the jobs associated with the current AWS account that have a given status, specify the following status: <code>Submitted</code>, <code>Progressing</code>, <code>Complete</code>, <code>Canceled</code>, or <code>Error</code>.</p>"""
    ascending: NotRequired["aws_sdk_elastic_transcoder.types.ascending.Ascending"]
    """<p> To list jobs in chronological order by the date and time that they were submitted, enter <code>true</code>. To list jobs in reverse chronological order, enter <code>false</code>. </p>"""
    page_token: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p> When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobsByStatusRequest:
    out: ListJobsByStatusRequest = {}  # type: ignore[typeddict-item]
    return out
