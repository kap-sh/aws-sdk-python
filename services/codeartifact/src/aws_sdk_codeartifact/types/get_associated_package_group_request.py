"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetAssociatedPackageGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace


class GetAssociatedPackageGroupRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the package from which to get the associated package group. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> The format of the package from which to get the associated package group. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package from which to get the associated package group. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when getting associated package groups from packages of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p> The package from which to get the associated package group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedPackageGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssociatedPackageGroupRequest:
    out: GetAssociatedPackageGroupRequest = {}  # type: ignore[typeddict-item]
    return out
