"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.jobs_list
    import aws_sdk_mgn.types.pagination_token


class DescribeJobsResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_mgn.types.jobs_list.JobsList"]
    """<p>Request to describe Job log items.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe Job response by next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mgn.types.jobs_list

        out["items"] = aws_sdk_mgn.types.jobs_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobsResponse:
    out: DescribeJobsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_mgn.types.jobs_list

        out["items"] = aws_sdk_mgn.types.jobs_list.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
