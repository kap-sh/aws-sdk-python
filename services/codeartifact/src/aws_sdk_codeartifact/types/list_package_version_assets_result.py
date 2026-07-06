"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageVersionAssetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.asset_summary_list
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.package_version_revision
    import aws_sdk_codeartifact.types.pagination_token


class ListPackageVersionAssetsResult(TypedDict, closed=True):
    format: NotRequired["aws_sdk_codeartifact.types.package_format.PackageFormat"]
    """<p> The format of the package that contains the requested package version assets. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package version that contains the requested package version assets. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["aws_sdk_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package that contains the requested package version assets. </p>"""
    version: NotRequired["aws_sdk_codeartifact.types.package_version.PackageVersion"]
    """<p> The version of the package associated with the requested assets. </p>"""
    version_revision: NotRequired[
        "aws_sdk_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The current revision associated with the package version. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> If there are additional results, this is the token for the next set of results. </p>"""
    assets: NotRequired[
        "aws_sdk_codeartifact.types.asset_summary_list.AssetSummaryList"
    ]
    r"""<p> The returned list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\">AssetSummary</a> objects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionAssetsResult) -> dict:
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
    if "assets" in value:
        import aws_sdk_codeartifact.types.asset_summary_list

        out["assets"] = aws_sdk_codeartifact.types.asset_summary_list.serialize_json(
            value["assets"]
        )
    return out


def deserialize_json(data: dict) -> ListPackageVersionAssetsResult:
    out: ListPackageVersionAssetsResult = {}  # type: ignore[typeddict-item]
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
    if "assets" in data:
        import aws_sdk_codeartifact.types.asset_summary_list

        out["assets"] = aws_sdk_codeartifact.types.asset_summary_list.deserialize_json(
            data["assets"]
        )
    return out
