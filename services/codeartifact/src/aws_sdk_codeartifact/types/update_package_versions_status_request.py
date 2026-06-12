"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdatePackageVersionsStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version_list
    import aws_sdk_codeartifact.types.package_version_revision_map
    import aws_sdk_codeartifact.types.package_version_status
    import aws_sdk_codeartifact.types.repository_name


class UpdatePackageVersionsStatusRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository that contains the package versions with a status to be updated. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The repository that contains the package versions with the status you want to update. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> A format that specifies the type of the package with the statuses to update. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package version to be updated. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p> The name of the package with the version statuses to update. </p>"""
    versions: "aws_sdk_codeartifact.types.package_version_list.PackageVersionList"
    """<p> An array of strings that specify the versions of the package with the statuses to update. </p>"""
    version_revisions: NotRequired[
        "aws_sdk_codeartifact.types.package_version_revision_map.PackageVersionRevisionMap"
    ]
    """<p> A map of package versions and package version revisions. The map <code>key</code> is the package version (for example, <code>3.5.2</code>), and the map <code>value</code> is the package version revision. </p>"""
    expected_status: NotRequired[
        "aws_sdk_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    """<p> The package version’s expected status before it is updated. If <code>expectedStatus</code> is provided, the package version's status is updated only if its status at the time <code>UpdatePackageVersionsStatus</code> is called matches <code>expectedStatus</code>. </p>"""
    target_status: (
        "aws_sdk_codeartifact.types.package_version_status.PackageVersionStatus"
    )
    """<p> The status you want to change the package version status to. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageVersionsStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_codeartifact.types.package_version_list

    out["versions"] = aws_sdk_codeartifact.types.package_version_list.serialize_json(
        value["versions"]
    )
    if "version_revisions" in value:
        import aws_sdk_codeartifact.types.package_version_revision_map

        out["versionRevisions"] = (
            aws_sdk_codeartifact.types.package_version_revision_map.serialize_json(
                value["version_revisions"]
            )
        )
    if "expected_status" in value:
        import aws_sdk_codeartifact.types.package_version_status

        out["expectedStatus"] = (
            aws_sdk_codeartifact.types.package_version_status.serialize_json(
                value["expected_status"]
            )
        )
    import aws_sdk_codeartifact.types.package_version_status

    out["targetStatus"] = (
        aws_sdk_codeartifact.types.package_version_status.serialize_json(
            value["target_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePackageVersionsStatusRequest:
    out: UpdatePackageVersionsStatusRequest = {}  # type: ignore[typeddict-item]
    if "versions" in data:
        import aws_sdk_codeartifact.types.package_version_list

        out["versions"] = (
            aws_sdk_codeartifact.types.package_version_list.deserialize_json(
                data["versions"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePackageVersionsStatusRequest.versions required"
        )
    if "versionRevisions" in data:
        import aws_sdk_codeartifact.types.package_version_revision_map

        out["version_revisions"] = (
            aws_sdk_codeartifact.types.package_version_revision_map.deserialize_json(
                data["versionRevisions"]
            )
        )
    if "expectedStatus" in data:
        import aws_sdk_codeartifact.types.package_version_status

        out["expected_status"] = (
            aws_sdk_codeartifact.types.package_version_status.deserialize_json(
                data["expectedStatus"]
            )
        )
    if "targetStatus" in data:
        import aws_sdk_codeartifact.types.package_version_status

        out["target_status"] = (
            aws_sdk_codeartifact.types.package_version_status.deserialize_json(
                data["targetStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePackageVersionsStatusRequest.target_status required"
        )
    return out
