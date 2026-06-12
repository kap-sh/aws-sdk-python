"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageVersionDependenciesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_dependency_list
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.package_version_revision
    import aws_sdk_codeartifact.types.pagination_token


class ListPackageVersionDependenciesResult(TypedDict):
    format: NotRequired["aws_sdk_codeartifact.types.package_format.PackageFormat"]
    """<p> A format that specifies the type of the package that contains the returned dependencies. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package version that contains the returned dependencies. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when listing dependencies from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["aws_sdk_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package that contains the returned package versions dependencies. </p>"""
    version: NotRequired["aws_sdk_codeartifact.types.package_version.PackageVersion"]
    """<p> The version of the package that is specified in the request. </p>"""
    version_revision: NotRequired[
        "aws_sdk_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The current revision associated with the package version. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    dependencies: NotRequired[
        "aws_sdk_codeartifact.types.package_dependency_list.PackageDependencyList"
    ]
    """<p> The returned list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\">PackageDependency</a> objects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionDependenciesResult) -> dict:
    out: dict = {}
    if "format" in value:
        import aws_sdk_codeartifact.types.package_format

        out["format"] = aws_sdk_codeartifact.types.package_format.serialize_json(
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
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "dependencies" in value:
        import aws_sdk_codeartifact.types.package_dependency_list

        out["dependencies"] = (
            aws_sdk_codeartifact.types.package_dependency_list.serialize_json(
                value["dependencies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPackageVersionDependenciesResult:
    out: ListPackageVersionDependenciesResult = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_codeartifact.types.package_format

        out["format"] = aws_sdk_codeartifact.types.package_format.deserialize_json(
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
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "dependencies" in data:
        import aws_sdk_codeartifact.types.package_dependency_list

        out["dependencies"] = (
            aws_sdk_codeartifact.types.package_dependency_list.deserialize_json(
                data["dependencies"]
            )
        )
    return out
