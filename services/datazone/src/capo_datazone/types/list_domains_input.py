"""Generated from Smithy shape ``com.amazonaws.datazone#ListDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_status
    import capo_datazone.types.max_results_for_list_domains
    import capo_datazone.types.pagination_token


class ListDomainsInput(TypedDict, closed=True):
    status: NotRequired["capo_datazone.types.domain_status.DomainStatus"]
    """<p>The status of the data source.</p>"""
    max_results: NotRequired[
        "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
    ]
    """<p>The maximum number of domains to return in a single call to <code>ListDomains</code>. When the number of domains to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of domains is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of domains, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainsInput:
    out: ListDomainsInput = {}  # type: ignore[typeddict-item]
    return out
