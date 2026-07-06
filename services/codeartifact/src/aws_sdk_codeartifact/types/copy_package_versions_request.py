"""Generated from Smithy shape ``com.amazonaws.codeartifact#CopyPackageVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.boolean_optional
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version_list
    import aws_sdk_codeartifact.types.package_version_revision_map
    import aws_sdk_codeartifact.types.repository_name


class CopyPackageVersionsRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the source and destination repositories. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    source_repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository that contains the package versions to be copied. </p>"""
    destination_repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository into which package versions are copied. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> The format of the package versions to be copied. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package versions to be copied. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when copying package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "aws_sdk_codeartifact.types.package_name.PackageName"
    """<p> The name of the package that contains the versions to be copied. </p>"""
    versions: NotRequired[
        "aws_sdk_codeartifact.types.package_version_list.PackageVersionList"
    ]
    """<p> The versions of the package to be copied. </p> <note> <p> You must specify <code>versions</code> or <code>versionRevisions</code>. You cannot specify both. </p> </note>"""
    version_revisions: NotRequired[
        "aws_sdk_codeartifact.types.package_version_revision_map.PackageVersionRevisionMap"
    ]
    """<p> A list of key-value pairs. The keys are package versions and the values are package version revisions. A <code>CopyPackageVersion</code> operation succeeds if the specified versions in the source repository match the specified package version revision. </p> <note> <p> You must specify <code>versions</code> or <code>versionRevisions</code>. You cannot specify both. </p> </note>"""
    allow_overwrite: NotRequired[
        "aws_sdk_codeartifact.types.boolean_optional.BooleanOptional"
    ]
    """<p> Set to true to overwrite a package version that already exists in the destination repository. If set to false and the package version already exists in the destination repository, the package version is returned in the <code>failedVersions</code> field of the response with an <code>ALREADY_EXISTS</code> error code. </p>"""
    include_from_upstream: NotRequired[
        "aws_sdk_codeartifact.types.boolean_optional.BooleanOptional"
    ]
    r"""<p> Set to true to copy packages from repositories that are upstream from the source repository to the destination repository. The default setting is false. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\">Working with upstream repositories</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyPackageVersionsRequest) -> dict:
    out: dict = {}
    if "versions" in value:
        import aws_sdk_codeartifact.types.package_version_list

        out["versions"] = (
            aws_sdk_codeartifact.types.package_version_list.serialize_json(
                value["versions"]
            )
        )
    if "version_revisions" in value:
        import aws_sdk_codeartifact.types.package_version_revision_map

        out["versionRevisions"] = (
            aws_sdk_codeartifact.types.package_version_revision_map.serialize_json(
                value["version_revisions"]
            )
        )
    if "allow_overwrite" in value:
        out["allowOverwrite"] = value["allow_overwrite"]
    if "include_from_upstream" in value:
        out["includeFromUpstream"] = value["include_from_upstream"]
    return out


def deserialize_json(data: dict) -> CopyPackageVersionsRequest:
    out: CopyPackageVersionsRequest = {}  # type: ignore[typeddict-item]
    if "versions" in data:
        import aws_sdk_codeartifact.types.package_version_list

        out["versions"] = (
            aws_sdk_codeartifact.types.package_version_list.deserialize_json(
                data["versions"]
            )
        )
    if "versionRevisions" in data:
        import aws_sdk_codeartifact.types.package_version_revision_map

        out["version_revisions"] = (
            aws_sdk_codeartifact.types.package_version_revision_map.deserialize_json(
                data["versionRevisions"]
            )
        )
    if "allowOverwrite" in data:
        out["allow_overwrite"] = data["allowOverwrite"]
    if "includeFromUpstream" in data:
        out["include_from_upstream"] = data["includeFromUpstream"]
    return out
