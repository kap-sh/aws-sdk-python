"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobLogItemsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.job_id
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token


class DescribeJobLogItemsRequest(TypedDict):
    job_id: "aws_sdk_mgn.types.job_id.JobID"
    """<p>Request to describe Job log job ID.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>Request to describe Job log item maximum results.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe Job log next token.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Request to describe Job log Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobLogItemsRequest) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
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
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
