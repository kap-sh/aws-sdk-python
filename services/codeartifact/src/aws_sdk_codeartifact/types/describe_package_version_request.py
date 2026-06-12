"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribePackageVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.repository_name


class DescribePackageVersionRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository that contains the package version. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository that contains the package version. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> A format that specifies the type of the requested package version. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the requested package version. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when requesting package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p> The name of the requested package version. </p>"""
    package_version: "aws_sdk_codeartifact.types.package_version.PackageVersion"
    """<p> A string that contains the package version (for example, <code>3.5.2</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePackageVersionRequest:
    out: DescribePackageVersionRequest = {}  # type: ignore[typeddict-item]
    return out
