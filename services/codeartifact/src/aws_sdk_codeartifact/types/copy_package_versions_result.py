"""Generated from Smithy shape ``com.amazonaws.codeartifact#CopyPackageVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_version_error_map
    import aws_sdk_codeartifact.types.successful_package_version_info_map


class CopyPackageVersionsResult(TypedDict, closed=True):
    successful_versions: NotRequired[
        "aws_sdk_codeartifact.types.successful_package_version_info_map.SuccessfulPackageVersionInfoMap"
    ]
    """<p> A list of the package versions that were successfully copied to your repository. </p>"""
    failed_versions: NotRequired[
        "aws_sdk_codeartifact.types.package_version_error_map.PackageVersionErrorMap"
    ]
    """<p> A map of package versions that failed to copy and their error codes. The possible error codes are in the <code>PackageVersionError</code> data type. They are: </p> <ul> <li> <p> <code>ALREADY_EXISTS</code> </p> </li> <li> <p> <code>MISMATCHED_REVISION</code> </p> </li> <li> <p> <code>MISMATCHED_STATUS</code> </p> </li> <li> <p> <code>NOT_ALLOWED</code> </p> </li> <li> <p> <code>NOT_FOUND</code> </p> </li> <li> <p> <code>SKIPPED</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyPackageVersionsResult) -> dict:
    out: dict = {}
    if "successful_versions" in value:
        import aws_sdk_codeartifact.types.successful_package_version_info_map

        out["successfulVersions"] = (
            aws_sdk_codeartifact.types.successful_package_version_info_map.serialize_json(
                value["successful_versions"]
            )
        )
    if "failed_versions" in value:
        import aws_sdk_codeartifact.types.package_version_error_map

        out["failedVersions"] = (
            aws_sdk_codeartifact.types.package_version_error_map.serialize_json(
                value["failed_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CopyPackageVersionsResult:
    out: CopyPackageVersionsResult = {}  # type: ignore[typeddict-item]
    if "successfulVersions" in data:
        import aws_sdk_codeartifact.types.successful_package_version_info_map

        out["successful_versions"] = (
            aws_sdk_codeartifact.types.successful_package_version_info_map.deserialize_json(
                data["successfulVersions"]
            )
        )
    if "failedVersions" in data:
        import aws_sdk_codeartifact.types.package_version_error_map

        out["failed_versions"] = (
            aws_sdk_codeartifact.types.package_version_error_map.deserialize_json(
                data["failedVersions"]
            )
        )
    return out
