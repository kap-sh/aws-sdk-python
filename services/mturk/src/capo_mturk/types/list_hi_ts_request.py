"""Generated from Smithy shape ``com.amazonaws.mturk#ListHITsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.pagination_token
    import capo_mturk.types.result_size


class ListHITsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    """<p>Pagination token</p>"""
    max_results: NotRequired["capo_mturk.types.result_size.ResultSize"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHITsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHITsRequest:
    out: ListHITsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
