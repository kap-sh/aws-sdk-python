"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListSubPackageGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.list_package_groups_max_results
    import capo_codeartifact.types.package_group_pattern
    import capo_codeartifact.types.pagination_token


class ListSubPackageGroupsRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain which contains the package group from which to list sub package groups. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern"
    """<p> The pattern of the package group from which to list sub package groups. </p>"""
    max_results: NotRequired[
        "capo_codeartifact.types.list_package_groups_max_results.ListPackageGroupsMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubPackageGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubPackageGroupsRequest:
    out: ListSubPackageGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
