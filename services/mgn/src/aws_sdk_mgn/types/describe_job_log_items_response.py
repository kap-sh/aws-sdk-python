"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobLogItemsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.job_logs
    import aws_sdk_mgn.types.pagination_token


class DescribeJobLogItemsResponse(TypedDict):
    items: NotRequired["aws_sdk_mgn.types.job_logs.JobLogs"]
    """<p>Request to describe Job log response items.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe Job log response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobLogItemsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mgn.types.job_logs

        out["items"] = aws_sdk_mgn.types.job_logs.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobLogItemsResponse:
    out: DescribeJobLogItemsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_mgn.types.job_logs

        out["items"] = aws_sdk_mgn.types.job_logs.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
