"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.list_package_versions_max_results
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version_origin_type
    import aws_sdk_codeartifact.types.package_version_sort_type
    import aws_sdk_codeartifact.types.package_version_status
    import aws_sdk_codeartifact.types.pagination_token
    import aws_sdk_codeartifact.types.repository_name


class ListPackageVersionsRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository that contains the requested package versions. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository that contains the requested package versions. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> The format of the package versions you want to list. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when deleting package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p> The name of the package for which you want to request package versions. </p>"""
    status: NotRequired[
        "aws_sdk_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    """<p> A string that filters the requested package versions by status. </p>"""
    sort_by: NotRequired[
        "aws_sdk_codeartifact.types.package_version_sort_type.PackageVersionSortType"
    ]
    """<p> How to sort the requested list of package versions. </p>"""
    max_results: NotRequired[
        "aws_sdk_codeartifact.types.list_package_versions_max_results.ListPackageVersionsMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    origin_type: NotRequired[
        "aws_sdk_codeartifact.types.package_version_origin_type.PackageVersionOriginType"
    ]
    """<p>The <code>originType</code> used to filter package versions. Only package versions with the provided <code>originType</code> will be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackageVersionsRequest:
    out: ListPackageVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
