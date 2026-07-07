"""Generated from Smithy shape ``com.amazonaws.macie2#ListAutomatedDiscoveryAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.max_results


class ListAutomatedDiscoveryAccountsRequest(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>The Amazon Web Services account ID for each account, for as many as 50 accounts. To retrieve the status for multiple accounts, append the accountIds parameter and argument for each account, separated by an ampersand (&amp;). To retrieve the status for all the accounts in an organization, omit this parameter.</p>"""
    max_results: NotRequired["aws_sdk_macie2.types.max_results.MaxResults"]
    """<p>The maximum number of items to include in each page of a paginated response.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedDiscoveryAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAutomatedDiscoveryAccountsRequest:
    out: ListAutomatedDiscoveryAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
