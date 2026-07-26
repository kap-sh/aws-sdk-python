"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetPackageVersionReadmeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_revision
    import capo_codeartifact.types.string


class GetPackageVersionReadmeResult(TypedDict, closed=True):
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p> The format of the package with the requested readme file. </p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package version with the requested readme file. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package that contains the returned readme file. </p>"""
    version: NotRequired["capo_codeartifact.types.package_version.PackageVersion"]
    """<p> The version of the package with the requested readme file. </p>"""
    version_revision: NotRequired[
        "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The current revision associated with the package version. </p>"""
    readme: NotRequired["capo_codeartifact.types.string.String"]
    """<p> The text of the returned readme file. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionReadmeResult) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.serialize_json(
            value["format"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "package" in value:
        out["package"] = value["package"]
    if "version" in value:
        out["version"] = value["version"]
    if "version_revision" in value:
        out["versionRevision"] = value["version_revision"]
    if "readme" in value:
        out["readme"] = value["readme"]
    return out


def deserialize_json(data: dict) -> GetPackageVersionReadmeResult:
    out: GetPackageVersionReadmeResult = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "package" in data:
        out["package"] = data["package"]
    if "version" in data:
        out["version"] = data["version"]
    if "versionRevision" in data:
        out["version_revision"] = data["versionRevision"]
    if "readme" in data:
        out["readme"] = data["readme"]
    return out
