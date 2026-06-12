"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseAssetGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn


class DeleteLicenseAssetGroupRequest(TypedDict):
    license_asset_group_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseAssetGroupRequest) -> dict:
    out: dict = {}
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseAssetGroupRequest:
    out: DeleteLicenseAssetGroupRequest = {}  # type: ignore[typeddict-item]
    if "LicenseAssetGroupArn" in data:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        raise DeserializationError(
            "DeleteLicenseAssetGroupRequest.license_asset_group_arn required"
        )
    return out
