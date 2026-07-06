"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageVersionDependenciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.pagination_token
    import aws_sdk_codeartifact.types.repository_name


class ListPackageVersionDependenciesRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository that contains the requested package version dependencies. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository that contains the requested package version. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> The format of the package with the requested dependencies. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package version with the requested dependencies. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when listing dependencies from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p> The name of the package versions' package. </p>"""
    package_version: "aws_sdk_codeartifact.types.package_version.PackageVersion"
    """<p> A string that contains the package version (for example, <code>3.5.2</code>). </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionDependenciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackageVersionDependenciesRequest:
    out: ListPackageVersionDependenciesRequest = {}  # type: ignore[typeddict-item]
    return out
