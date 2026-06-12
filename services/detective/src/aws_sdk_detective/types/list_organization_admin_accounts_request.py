"""Generated from Smithy shape ``com.amazonaws.detective#ListOrganizationAdminAccountsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.member_results_limit
    import aws_sdk_detective.types.pagination_token


class ListOrganizationAdminAccountsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_detective.types.pagination_token.PaginationToken"]
    """<p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_detective.types.member_results_limit.MemberResultsLimit"
    ]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationAdminAccountsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListOrganizationAdminAccountsRequest:
    out: ListOrganizationAdminAccountsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
