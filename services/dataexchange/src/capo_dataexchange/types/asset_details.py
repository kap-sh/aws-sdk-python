"""Generated from Smithy shape ``com.amazonaws.dataexchange#AssetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.api_gateway_api_asset
    import capo_dataexchange.types.lake_formation_data_permission_asset
    import capo_dataexchange.types.redshift_data_share_asset
    import capo_dataexchange.types.s3_data_access_asset
    import capo_dataexchange.types.s3_snapshot_asset


class AssetDetails(TypedDict, closed=True):
    s3_snapshot_asset: NotRequired[
        "capo_dataexchange.types.s3_snapshot_asset.S3SnapshotAsset"
    ]
    """<p>The Amazon S3 object that is the asset.</p>"""
    redshift_data_share_asset: NotRequired[
        "capo_dataexchange.types.redshift_data_share_asset.RedshiftDataShareAsset"
    ]
    """<p>The Amazon Redshift datashare that is the asset.</p>"""
    api_gateway_api_asset: NotRequired[
        "capo_dataexchange.types.api_gateway_api_asset.ApiGatewayApiAsset"
    ]
    """<p>Information about the API Gateway API asset.</p>"""
    s3_data_access_asset: NotRequired[
        "capo_dataexchange.types.s3_data_access_asset.S3DataAccessAsset"
    ]
    """<p>The Amazon S3 data access that is the asset.</p>"""
    lake_formation_data_permission_asset: NotRequired[
        "capo_dataexchange.types.lake_formation_data_permission_asset.LakeFormationDataPermissionAsset"
    ]
    """<p>The AWS Lake Formation data permission that is the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetDetails) -> dict:
    out: dict = {}
    if "s3_snapshot_asset" in value:
        import capo_dataexchange.types.s3_snapshot_asset

        out["S3SnapshotAsset"] = (
            capo_dataexchange.types.s3_snapshot_asset.serialize_json(
                value["s3_snapshot_asset"]
            )
        )
    if "redshift_data_share_asset" in value:
        import capo_dataexchange.types.redshift_data_share_asset

        out["RedshiftDataShareAsset"] = (
            capo_dataexchange.types.redshift_data_share_asset.serialize_json(
                value["redshift_data_share_asset"]
            )
        )
    if "api_gateway_api_asset" in value:
        import capo_dataexchange.types.api_gateway_api_asset

        out["ApiGatewayApiAsset"] = (
            capo_dataexchange.types.api_gateway_api_asset.serialize_json(
                value["api_gateway_api_asset"]
            )
        )
    if "s3_data_access_asset" in value:
        import capo_dataexchange.types.s3_data_access_asset

        out["S3DataAccessAsset"] = (
            capo_dataexchange.types.s3_data_access_asset.serialize_json(
                value["s3_data_access_asset"]
            )
        )
    if "lake_formation_data_permission_asset" in value:
        import capo_dataexchange.types.lake_formation_data_permission_asset

        out["LakeFormationDataPermissionAsset"] = (
            capo_dataexchange.types.lake_formation_data_permission_asset.serialize_json(
                value["lake_formation_data_permission_asset"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetDetails:
    out: AssetDetails = {}  # type: ignore[typeddict-item]
    if "S3SnapshotAsset" in data:
        import capo_dataexchange.types.s3_snapshot_asset

        out["s3_snapshot_asset"] = (
            capo_dataexchange.types.s3_snapshot_asset.deserialize_json(
                data["S3SnapshotAsset"]
            )
        )
    if "RedshiftDataShareAsset" in data:
        import capo_dataexchange.types.redshift_data_share_asset

        out["redshift_data_share_asset"] = (
            capo_dataexchange.types.redshift_data_share_asset.deserialize_json(
                data["RedshiftDataShareAsset"]
            )
        )
    if "ApiGatewayApiAsset" in data:
        import capo_dataexchange.types.api_gateway_api_asset

        out["api_gateway_api_asset"] = (
            capo_dataexchange.types.api_gateway_api_asset.deserialize_json(
                data["ApiGatewayApiAsset"]
            )
        )
    if "S3DataAccessAsset" in data:
        import capo_dataexchange.types.s3_data_access_asset

        out["s3_data_access_asset"] = (
            capo_dataexchange.types.s3_data_access_asset.deserialize_json(
                data["S3DataAccessAsset"]
            )
        )
    if "LakeFormationDataPermissionAsset" in data:
        import capo_dataexchange.types.lake_formation_data_permission_asset

        out["lake_formation_data_permission_asset"] = (
            capo_dataexchange.types.lake_formation_data_permission_asset.deserialize_json(
                data["LakeFormationDataPermissionAsset"]
            )
        )
    return out
