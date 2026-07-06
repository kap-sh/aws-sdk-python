"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeletePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.repository_name


class DeletePackageRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p>The name of the domain that contains the package to delete.</p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the package to delete.</p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p>The format of the requested package to delete.</p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when deleting packages of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p>The name of the package to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageRequest:
    out: DeletePackageRequest = {}  # type: ignore[typeddict-item]
    return out
