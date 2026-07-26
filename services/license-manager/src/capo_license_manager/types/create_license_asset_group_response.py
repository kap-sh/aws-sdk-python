"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseAssetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.string


class CreateLicenseAssetGroupResponse(TypedDict, closed=True):
    license_asset_group_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""
    status: "capo_license_manager.types.string.String"
    """<p>License asset group status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseAssetGroupResponse) -> dict:
    out: dict = {}
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseAssetGroupResponse:
    out: CreateLicenseAssetGroupResponse = {}  # type: ignore[typeddict-item]
    if "LicenseAssetGroupArn" in data:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        raise DeserializationError(
            "CreateLicenseAssetGroupResponse.license_asset_group_arn required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("CreateLicenseAssetGroupResponse.status required")
    return out
