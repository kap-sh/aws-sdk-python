"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListRepositoriesInDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.list_repositories_in_domain_max_results
    import capo_codeartifact.types.pagination_token
    import capo_codeartifact.types.repository_name


class ListRepositoriesInDomainRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the returned list of repositories. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    administrator_account: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID. </p>"""
    repository_prefix: NotRequired[
        "capo_codeartifact.types.repository_name.RepositoryName"
    ]
    """<p> A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned. </p>"""
    max_results: NotRequired[
        "capo_codeartifact.types.list_repositories_in_domain_max_results.ListRepositoriesInDomainMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRepositoriesInDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRepositoriesInDomainRequest:
    out: ListRepositoriesInDomainRequest = {}  # type: ignore[typeddict-item]
    return out
