"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.iso8601_date_time
    import aws_sdk_license_manager.types.license_deletion_status


class DeleteLicenseResponse(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_license_manager.types.license_deletion_status.LicenseDeletionStatus"
    ]
    """<p>License status.</p>"""
    deletion_date: NotRequired[
        "aws_sdk_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Date when the license is deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_license_manager.types.license_deletion_status

        out["Status"] = (
            aws_sdk_license_manager.types.license_deletion_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "deletion_date" in value:
        out["DeletionDate"] = value["deletion_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseResponse:
    out: DeleteLicenseResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_license_manager.types.license_deletion_status

        out["status"] = (
            aws_sdk_license_manager.types.license_deletion_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "DeletionDate" in data:
        out["deletion_date"] = data["DeletionDate"]
    return out
