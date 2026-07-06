"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.list_package_groups_max_results
    import aws_sdk_codeartifact.types.package_group_pattern_prefix
    import aws_sdk_codeartifact.types.pagination_token


class ListPackageGroupsRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The domain for which you want to list package groups. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    max_results: NotRequired[
        "aws_sdk_codeartifact.types.list_package_groups_max_results.ListPackageGroupsMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    prefix: NotRequired[
        "aws_sdk_codeartifact.types.package_group_pattern_prefix.PackageGroupPatternPrefix"
    ]
    """<p> A prefix for which to search package groups. When included, <code>ListPackageGroups</code> will return only package groups with patterns that match the prefix. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackageGroupsRequest:
    out: ListPackageGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
