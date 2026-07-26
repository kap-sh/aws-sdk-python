"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobLogItemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.job_logs
    import capo_mgn.types.pagination_token


class DescribeJobLogItemsResponse(TypedDict, closed=True):
    items: NotRequired["capo_mgn.types.job_logs.JobLogs"]
    """<p>Request to describe Job log response items.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe Job log response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobLogItemsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.job_logs

        out["items"] = capo_mgn.types.job_logs.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobLogItemsResponse:
    out: DescribeJobLogItemsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_mgn.types.job_logs

        out["items"] = capo_mgn.types.job_logs.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
