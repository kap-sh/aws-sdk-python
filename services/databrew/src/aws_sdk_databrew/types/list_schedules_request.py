"""Generated from Smithy shape ``com.amazonaws.databrew#ListSchedulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_name
    import aws_sdk_databrew.types.max_results100
    import aws_sdk_databrew.types.next_token


class ListSchedulesRequest(TypedDict):
    job_name: NotRequired["aws_sdk_databrew.types.job_name.JobName"]
    """<p>The name of the job that these schedules apply to.</p>"""
    max_results: NotRequired["aws_sdk_databrew.types.max_results100.MaxResults100"]
    """<p>The maximum number of results to return in this request. </p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchedulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSchedulesRequest:
    out: ListSchedulesRequest = {}  # type: ignore[typeddict-item]
    return out
