"""Generated from Smithy shape ``com.amazonaws.codeartifact#PublishPackageVersionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.asset_summary
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.package_version_revision
    import aws_sdk_codeartifact.types.package_version_status


class PublishPackageVersionResult(TypedDict):
    format: NotRequired["aws_sdk_codeartifact.types.package_format.PackageFormat"]
    """<p>The format of the package version.</p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package version.</p>"""
    package: NotRequired["aws_sdk_codeartifact.types.package_name.PackageName"]
    """<p>The name of the package.</p>"""
    version: NotRequired["aws_sdk_codeartifact.types.package_version.PackageVersion"]
    """<p>The version of the package.</p>"""
    version_revision: NotRequired[
        "aws_sdk_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p>The revision of the package version.</p>"""
    status: NotRequired[
        "aws_sdk_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    """<p>A string that contains the status of the package version. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\">Package version status</a> in the <i>CodeArtifact User Guide</i>.</p>"""
    asset: NotRequired["aws_sdk_codeartifact.types.asset_summary.AssetSummary"]
    """<p>An <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\">AssetSummary</a> for the published asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishPackageVersionResult) -> dict:
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
    if "status" in value:
        import aws_sdk_codeartifact.types.package_version_status

        out["status"] = (
            aws_sdk_codeartifact.types.package_version_status.serialize_json(
                value["status"]
            )
        )
    if "asset" in value:
        import aws_sdk_codeartifact.types.asset_summary

        out["asset"] = aws_sdk_codeartifact.types.asset_summary.serialize_json(
            value["asset"]
        )
    return out


def deserialize_json(data: dict) -> PublishPackageVersionResult:
    out: PublishPackageVersionResult = {}  # type: ignore[typeddict-item]
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
    if "status" in data:
        import aws_sdk_codeartifact.types.package_version_status

        out["status"] = (
            aws_sdk_codeartifact.types.package_version_status.deserialize_json(
                data["status"]
            )
        )
    if "asset" in data:
        import aws_sdk_codeartifact.types.asset_summary

        out["asset"] = aws_sdk_codeartifact.types.asset_summary.deserialize_json(
            data["asset"]
        )
    return out
