"""Generated from Smithy shape ``com.amazonaws.licensemanager#Asset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.date_time
    import capo_license_manager.types.string


class Asset(TypedDict, closed=True):
    asset_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the asset.</p>"""
    latest_asset_discovery_time: NotRequired[
        "capo_license_manager.types.date_time.DateTime"
    ]
    """<p>Latest asset discovery time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Asset) -> dict:
    out: dict = {}
    if "asset_arn" in value:
        out["AssetArn"] = value["asset_arn"]
    if "latest_asset_discovery_time" in value:
        import capo_license_manager.types.date_time

        out["LatestAssetDiscoveryTime"] = (
            capo_license_manager.types.date_time.serialize_aws_json_1_1(
                value["latest_asset_discovery_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Asset:
    out: Asset = {}  # type: ignore[typeddict-item]
    if "AssetArn" in data:
        out["asset_arn"] = data["AssetArn"]
    if "LatestAssetDiscoveryTime" in data:
        import capo_license_manager.types.date_time

        out["latest_asset_discovery_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LatestAssetDiscoveryTime"]
            )
        )
    return out
