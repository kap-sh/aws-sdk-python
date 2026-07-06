"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListAssociatedPackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.boolean_optional
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.list_packages_max_results
    import aws_sdk_codeartifact.types.package_group_pattern
    import aws_sdk_codeartifact.types.pagination_token


class ListAssociatedPackagesRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the package group from which to list associated packages. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: (
        "aws_sdk_codeartifact.types.package_group_pattern.PackageGroupPattern"
    )
    """<p> The pattern of the package group from which to list associated packages. </p>"""
    max_results: NotRequired[
        "aws_sdk_codeartifact.types.list_packages_max_results.ListPackagesMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    preview: NotRequired["aws_sdk_codeartifact.types.boolean_optional.BooleanOptional"]
    """<p> When this flag is included, <code>ListAssociatedPackages</code> will return a list of packages that would be associated with a package group, even if it does not exist. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedPackagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedPackagesRequest:
    out: ListAssociatedPackagesRequest = {}  # type: ignore[typeddict-item]
    return out
