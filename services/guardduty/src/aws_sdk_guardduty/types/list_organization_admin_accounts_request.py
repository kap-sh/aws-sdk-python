"""Generated from Smithy shape ``com.amazonaws.guardduty#ListOrganizationAdminAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.max_results
    import aws_sdk_guardduty.types.string


class ListOrganizationAdminAccountsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_guardduty.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationAdminAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOrganizationAdminAccountsRequest:
    out: ListOrganizationAdminAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
