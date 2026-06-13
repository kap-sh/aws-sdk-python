"""Generated from Smithy shape ``com.amazonaws.datazone#ListAccountsInAccountPoolInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_id
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token


class ListAccountsInAccountPoolInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which the accounts in the specified account pool are to be listed.</p>"""
    identifier: "aws_sdk_datazone.types.account_pool_id.AccountPoolId"
    """<p>The ID of the account pool whose accounts are to be listed.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of accounts is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of accounts, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of accounts to return in a single call to ListAccountsInAccountPool. When the number of accounts to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountsInAccountPoolInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccountsInAccountPoolInput:
    out: ListAccountsInAccountPoolInput = {}  # type: ignore[typeddict-item]
    return out
