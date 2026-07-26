"""Generated from Smithy shape ``com.amazonaws.codeartifact#PublishPackageVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.asset_summary
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_revision
    import capo_codeartifact.types.package_version_status


class PublishPackageVersionResult(TypedDict, closed=True):
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p>The format of the package version.</p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package version.</p>"""
    package: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p>The name of the package.</p>"""
    version: NotRequired["capo_codeartifact.types.package_version.PackageVersion"]
    """<p>The version of the package.</p>"""
    version_revision: NotRequired[
        "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p>The revision of the package version.</p>"""
    status: NotRequired[
        "capo_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    r"""<p>A string that contains the status of the package version. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\">Package version status</a> in the <i>CodeArtifact User Guide</i>.</p>"""
    asset: NotRequired["capo_codeartifact.types.asset_summary.AssetSummary"]
    r"""<p>An <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\">AssetSummary</a> for the published asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishPackageVersionResult) -> dict:
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
    if "status" in value:
        import capo_codeartifact.types.package_version_status

        out["status"] = capo_codeartifact.types.package_version_status.serialize_json(
            value["status"]
        )
    if "asset" in value:
        import capo_codeartifact.types.asset_summary

        out["asset"] = capo_codeartifact.types.asset_summary.serialize_json(
            value["asset"]
        )
    return out


def deserialize_json(data: dict) -> PublishPackageVersionResult:
    out: PublishPackageVersionResult = {}  # type: ignore[typeddict-item]
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
    if "status" in data:
        import capo_codeartifact.types.package_version_status

        out["status"] = capo_codeartifact.types.package_version_status.deserialize_json(
            data["status"]
        )
    if "asset" in data:
        import capo_codeartifact.types.asset_summary

        out["asset"] = capo_codeartifact.types.asset_summary.deserialize_json(
            data["asset"]
        )
    return out
