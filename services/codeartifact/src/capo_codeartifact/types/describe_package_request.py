"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.repository_name


class DescribePackageRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p>The name of the domain that contains the repository that contains the package.</p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the requested package. </p>"""
    format: "capo_codeartifact.types.package_format.PackageFormat"
    """<p>A format that specifies the type of the requested package.</p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when requesting packages of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "capo_codeartifact.types.package_name.PackageName"
    """<p>The name of the requested package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePackageRequest:
    out: DescribePackageRequest = {}  # type: ignore[typeddict-item]
    return out
