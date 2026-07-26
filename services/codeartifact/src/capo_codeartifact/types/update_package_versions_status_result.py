"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdatePackageVersionsStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version_error_map
    import capo_codeartifact.types.successful_package_version_info_map


class UpdatePackageVersionsStatusResult(TypedDict, closed=True):
    successful_versions: NotRequired[
        "capo_codeartifact.types.successful_package_version_info_map.SuccessfulPackageVersionInfoMap"
    ]
    """<p> A list of <code>PackageVersionError</code> objects, one for each package version with a status that failed to update. </p>"""
    failed_versions: NotRequired[
        "capo_codeartifact.types.package_version_error_map.PackageVersionErrorMap"
    ]
    """<p> A list of <code>SuccessfulPackageVersionInfo</code> objects, one for each package version with a status that successfully updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageVersionsStatusResult) -> dict:
    out: dict = {}
    if "successful_versions" in value:
        import capo_codeartifact.types.successful_package_version_info_map

        out["successfulVersions"] = (
            capo_codeartifact.types.successful_package_version_info_map.serialize_json(
                value["successful_versions"]
            )
        )
    if "failed_versions" in value:
        import capo_codeartifact.types.package_version_error_map

        out["failedVersions"] = (
            capo_codeartifact.types.package_version_error_map.serialize_json(
                value["failed_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageVersionsStatusResult:
    out: UpdatePackageVersionsStatusResult = {}  # type: ignore[typeddict-item]
    if "successfulVersions" in data:
        import capo_codeartifact.types.successful_package_version_info_map

        out["successful_versions"] = (
            capo_codeartifact.types.successful_package_version_info_map.deserialize_json(
                data["successfulVersions"]
            )
        )
    if "failedVersions" in data:
        import capo_codeartifact.types.package_version_error_map

        out["failed_versions"] = (
            capo_codeartifact.types.package_version_error_map.deserialize_json(
                data["failedVersions"]
            )
        )
    return out
