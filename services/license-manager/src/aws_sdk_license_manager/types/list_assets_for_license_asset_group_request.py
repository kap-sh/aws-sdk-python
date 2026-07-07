"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListAssetsForLicenseAssetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_integer
    import aws_sdk_license_manager.types.string


class ListAssetsForLicenseAssetGroupRequest(TypedDict, closed=True):
    license_asset_group_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""
    asset_type: "aws_sdk_license_manager.types.string.String"
    """<p>Asset type. The possible values are <code>Instance</code> | <code>License</code> | <code>LicenseConfiguration</code>.</p>"""
    max_results: NotRequired["aws_sdk_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssetsForLicenseAssetGroupRequest) -> dict:
    out: dict = {}
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    out["AssetType"] = value["asset_type"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssetsForLicenseAssetGroupRequest:
    out: ListAssetsForLicenseAssetGroupRequest = {}  # type: ignore[typeddict-item]
    if "LicenseAssetGroupArn" in data:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        raise DeserializationError(
            "ListAssetsForLicenseAssetGroupRequest.license_asset_group_arn required"
        )
    if "AssetType" in data:
        out["asset_type"] = data["AssetType"]
    else:
        raise DeserializationError(
            "ListAssetsForLicenseAssetGroupRequest.asset_type required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
