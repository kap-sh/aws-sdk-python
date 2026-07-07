"""Generated from Smithy shape ``com.amazonaws.drs#DescribeJobLogItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.job_id
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.strictly_positive_integer


class DescribeJobLogItemsRequest(TypedDict, closed=True):
    job_id: "aws_sdk_drs.types.job_id.JobID"
    """<p>The ID of the Job for which Job log items will be retrieved.</p>"""
    max_results: NotRequired[
        "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Maximum number of Job log items to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Job log items to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobLogItemsRequest) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobLogItemsRequest:
    out: DescribeJobLogItemsRequest = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    else:
        raise DeserializationError("DescribeJobLogItemsRequest.job_id required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
