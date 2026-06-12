"""Generated from Smithy shape ``com.amazonaws.licensemanager#Asset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.date_time
    import aws_sdk_license_manager.types.string


class Asset(TypedDict):
    asset_arn: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the asset.</p>"""
    latest_asset_discovery_time: NotRequired[
        "aws_sdk_license_manager.types.date_time.DateTime"
    ]
    """<p>Latest asset discovery time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Asset) -> dict:
    out: dict = {}
    if "asset_arn" in value:
        out["AssetArn"] = value["asset_arn"]
    if "latest_asset_discovery_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["LatestAssetDiscoveryTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["latest_asset_discovery_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Asset:
    out: Asset = {}  # type: ignore[typeddict-item]
    if "AssetArn" in data:
        out["asset_arn"] = data["AssetArn"]
    if "LatestAssetDiscoveryTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["latest_asset_discovery_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LatestAssetDiscoveryTime"]
            )
        )
    return out
