"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseAssetGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class UpdateLicenseAssetGroupResponse(TypedDict):
    license_asset_group_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""
    status: "aws_sdk_license_manager.types.string.String"
    """<p>License asset group status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseAssetGroupResponse) -> dict:
    out: dict = {}
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseAssetGroupResponse:
    out: UpdateLicenseAssetGroupResponse = {}  # type: ignore[typeddict-item]
    if "LicenseAssetGroupArn" in data:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        raise DeserializationError(
            "UpdateLicenseAssetGroupResponse.license_asset_group_arn required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("UpdateLicenseAssetGroupResponse.status required")
    return out
