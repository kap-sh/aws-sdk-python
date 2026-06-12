"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageDependency``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.string


class PackageDependency(TypedDict):
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package that this package depends on. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["aws_sdk_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package that this package depends on. </p>"""
    dependency_type: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> The type of a package dependency. The possible values depend on the package type.</p> <ul> <li> <p>npm: <code>regular</code>, <code>dev</code>, <code>peer</code>, <code>optional</code> </p> </li> <li> <p>maven: <code>optional</code>, <code>parent</code>, <code>compile</code>, <code>runtime</code>, <code>test</code>, <code>system</code>, <code>provided</code>.</p> <note> <p>Note that <code>parent</code> is not a regular Maven dependency type; instead this is extracted from the <code><parent></code> element if one is defined in the package version's POM file.</p> </note> </li> <li> <p>nuget: The <code>dependencyType</code> field is never set for NuGet packages.</p> </li> <li> <p>pypi: <code>Requires-Dist</code> </p> </li> </ul>"""
    version_requirement: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> The required version, or version range, of the package that this package depends on. The version format is specific to the package type. For example, the following are possible valid required versions: <code>1.2.3</code>, <code>^2.3.4</code>, or <code>4.x</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageDependency) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "package" in value:
        out["package"] = value["package"]
    if "dependency_type" in value:
        out["dependencyType"] = value["dependency_type"]
    if "version_requirement" in value:
        out["versionRequirement"] = value["version_requirement"]
    return out


def deserialize_json(data: dict) -> PackageDependency:
    out: PackageDependency = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "package" in data:
        out["package"] = data["package"]
    if "dependencyType" in data:
        out["dependency_type"] = data["dependencyType"]
    if "versionRequirement" in data:
        out["version_requirement"] = data["versionRequirement"]
    return out
