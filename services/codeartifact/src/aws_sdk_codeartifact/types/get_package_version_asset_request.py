"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetPackageVersionAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.asset_name
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.package_version_revision
    import aws_sdk_codeartifact.types.repository_name


class GetPackageVersionAssetRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository that contains the package version with the requested asset. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The repository that contains the package version with the requested asset. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> A format that specifies the type of the package version with the requested asset file. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package version with the requested asset file. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when requesting assets from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p> The name of the package that contains the requested asset. </p>"""
    package_version: "aws_sdk_codeartifact.types.package_version.PackageVersion"
    """<p> A string that contains the package version (for example, <code>3.5.2</code>). </p>"""
    asset: "aws_sdk_codeartifact.types.asset_name.AssetName"
    """<p> The name of the requested asset. </p>"""
    package_version_revision: NotRequired[
        "aws_sdk_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The name of the package version revision that contains the requested asset. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionAssetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPackageVersionAssetRequest:
    out: GetPackageVersionAssetRequest = {}  # type: ignore[typeddict-item]
    return out
