"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.describe_jobs_request_filters
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token


class DescribeJobsRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_mgn.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
    ]
    """<p>Request to describe Job log filters.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>Request to describe job log items by max results.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe job log items by next token.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Request to describe job log items by Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_mgn.types.describe_jobs_request_filters

        out["filters"] = aws_sdk_mgn.types.describe_jobs_request_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DescribeJobsRequest:
    out: DescribeJobsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_mgn.types.describe_jobs_request_filters

        out["filters"] = (
            aws_sdk_mgn.types.describe_jobs_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
