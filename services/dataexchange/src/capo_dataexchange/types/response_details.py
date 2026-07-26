"""Generated from Smithy shape ``com.amazonaws.dataexchange#ResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.create_s3_data_access_from_s3_bucket_response_details
    import capo_dataexchange.types.export_asset_to_signed_url_response_details
    import capo_dataexchange.types.export_assets_to_s3_response_details
    import capo_dataexchange.types.export_revisions_to_s3_response_details
    import capo_dataexchange.types.import_asset_from_api_gateway_api_response_details
    import capo_dataexchange.types.import_asset_from_signed_url_response_details
    import capo_dataexchange.types.import_assets_from_lake_formation_tag_policy_response_details
    import capo_dataexchange.types.import_assets_from_redshift_data_shares_response_details
    import capo_dataexchange.types.import_assets_from_s3_response_details


class ResponseDetails(TypedDict, closed=True):
    export_asset_to_signed_url: NotRequired[
        "capo_dataexchange.types.export_asset_to_signed_url_response_details.ExportAssetToSignedUrlResponseDetails"
    ]
    """<p>Details for the export to signed URL response.</p>"""
    export_assets_to_s3: NotRequired[
        "capo_dataexchange.types.export_assets_to_s3_response_details.ExportAssetsToS3ResponseDetails"
    ]
    """<p>Details for the export to Amazon S3 response.</p>"""
    export_revisions_to_s3: NotRequired[
        "capo_dataexchange.types.export_revisions_to_s3_response_details.ExportRevisionsToS3ResponseDetails"
    ]
    """<p>Details for the export revisions to Amazon S3 response.</p>"""
    import_asset_from_signed_url: NotRequired[
        "capo_dataexchange.types.import_asset_from_signed_url_response_details.ImportAssetFromSignedUrlResponseDetails"
    ]
    """<p>Details for the import from signed URL response.</p>"""
    import_assets_from_s3: NotRequired[
        "capo_dataexchange.types.import_assets_from_s3_response_details.ImportAssetsFromS3ResponseDetails"
    ]
    """<p>Details for the import from Amazon S3 response.</p>"""
    import_assets_from_redshift_data_shares: NotRequired[
        "capo_dataexchange.types.import_assets_from_redshift_data_shares_response_details.ImportAssetsFromRedshiftDataSharesResponseDetails"
    ]
    """<p>Details from an import from Amazon Redshift datashare response.</p>"""
    import_asset_from_api_gateway_api: NotRequired[
        "capo_dataexchange.types.import_asset_from_api_gateway_api_response_details.ImportAssetFromApiGatewayApiResponseDetails"
    ]
    """<p>The response details.</p>"""
    create_s3_data_access_from_s3_bucket: NotRequired[
        "capo_dataexchange.types.create_s3_data_access_from_s3_bucket_response_details.CreateS3DataAccessFromS3BucketResponseDetails"
    ]
    """<p>Response details from the CreateS3DataAccessFromS3Bucket job.</p>"""
    import_assets_from_lake_formation_tag_policy: NotRequired[
        "capo_dataexchange.types.import_assets_from_lake_formation_tag_policy_response_details.ImportAssetsFromLakeFormationTagPolicyResponseDetails"
    ]
    """<p>Response details from the ImportAssetsFromLakeFormationTagPolicy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseDetails) -> dict:
    out: dict = {}
    if "export_asset_to_signed_url" in value:
        import capo_dataexchange.types.export_asset_to_signed_url_response_details

        out["ExportAssetToSignedUrl"] = (
            capo_dataexchange.types.export_asset_to_signed_url_response_details.serialize_json(
                value["export_asset_to_signed_url"]
            )
        )
    if "export_assets_to_s3" in value:
        import capo_dataexchange.types.export_assets_to_s3_response_details

        out["ExportAssetsToS3"] = (
            capo_dataexchange.types.export_assets_to_s3_response_details.serialize_json(
                value["export_assets_to_s3"]
            )
        )
    if "export_revisions_to_s3" in value:
        import capo_dataexchange.types.export_revisions_to_s3_response_details

        out["ExportRevisionsToS3"] = (
            capo_dataexchange.types.export_revisions_to_s3_response_details.serialize_json(
                value["export_revisions_to_s3"]
            )
        )
    if "import_asset_from_signed_url" in value:
        import capo_dataexchange.types.import_asset_from_signed_url_response_details

        out["ImportAssetFromSignedUrl"] = (
            capo_dataexchange.types.import_asset_from_signed_url_response_details.serialize_json(
                value["import_asset_from_signed_url"]
            )
        )
    if "import_assets_from_s3" in value:
        import capo_dataexchange.types.import_assets_from_s3_response_details

        out["ImportAssetsFromS3"] = (
            capo_dataexchange.types.import_assets_from_s3_response_details.serialize_json(
                value["import_assets_from_s3"]
            )
        )
    if "import_assets_from_redshift_data_shares" in value:
        import capo_dataexchange.types.import_assets_from_redshift_data_shares_response_details

        out["ImportAssetsFromRedshiftDataShares"] = (
            capo_dataexchange.types.import_assets_from_redshift_data_shares_response_details.serialize_json(
                value["import_assets_from_redshift_data_shares"]
            )
        )
    if "import_asset_from_api_gateway_api" in value:
        import capo_dataexchange.types.import_asset_from_api_gateway_api_response_details

        out["ImportAssetFromApiGatewayApi"] = (
            capo_dataexchange.types.import_asset_from_api_gateway_api_response_details.serialize_json(
                value["import_asset_from_api_gateway_api"]
            )
        )
    if "create_s3_data_access_from_s3_bucket" in value:
        import capo_dataexchange.types.create_s3_data_access_from_s3_bucket_response_details

        out["CreateS3DataAccessFromS3Bucket"] = (
            capo_dataexchange.types.create_s3_data_access_from_s3_bucket_response_details.serialize_json(
                value["create_s3_data_access_from_s3_bucket"]
            )
        )
    if "import_assets_from_lake_formation_tag_policy" in value:
        import capo_dataexchange.types.import_assets_from_lake_formation_tag_policy_response_details

        out["ImportAssetsFromLakeFormationTagPolicy"] = (
            capo_dataexchange.types.import_assets_from_lake_formation_tag_policy_response_details.serialize_json(
                value["import_assets_from_lake_formation_tag_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseDetails:
    out: ResponseDetails = {}  # type: ignore[typeddict-item]
    if "ExportAssetToSignedUrl" in data:
        import capo_dataexchange.types.export_asset_to_signed_url_response_details

        out["export_asset_to_signed_url"] = (
            capo_dataexchange.types.export_asset_to_signed_url_response_details.deserialize_json(
                data["ExportAssetToSignedUrl"]
            )
        )
    if "ExportAssetsToS3" in data:
        import capo_dataexchange.types.export_assets_to_s3_response_details

        out["export_assets_to_s3"] = (
            capo_dataexchange.types.export_assets_to_s3_response_details.deserialize_json(
                data["ExportAssetsToS3"]
            )
        )
    if "ExportRevisionsToS3" in data:
        import capo_dataexchange.types.export_revisions_to_s3_response_details

        out["export_revisions_to_s3"] = (
            capo_dataexchange.types.export_revisions_to_s3_response_details.deserialize_json(
                data["ExportRevisionsToS3"]
            )
        )
    if "ImportAssetFromSignedUrl" in data:
        import capo_dataexchange.types.import_asset_from_signed_url_response_details

        out["import_asset_from_signed_url"] = (
            capo_dataexchange.types.import_asset_from_signed_url_response_details.deserialize_json(
                data["ImportAssetFromSignedUrl"]
            )
        )
    if "ImportAssetsFromS3" in data:
        import capo_dataexchange.types.import_assets_from_s3_response_details

        out["import_assets_from_s3"] = (
            capo_dataexchange.types.import_assets_from_s3_response_details.deserialize_json(
                data["ImportAssetsFromS3"]
            )
        )
    if "ImportAssetsFromRedshiftDataShares" in data:
        import capo_dataexchange.types.import_assets_from_redshift_data_shares_response_details

        out["import_assets_from_redshift_data_shares"] = (
            capo_dataexchange.types.import_assets_from_redshift_data_shares_response_details.deserialize_json(
                data["ImportAssetsFromRedshiftDataShares"]
            )
        )
    if "ImportAssetFromApiGatewayApi" in data:
        import capo_dataexchange.types.import_asset_from_api_gateway_api_response_details

        out["import_asset_from_api_gateway_api"] = (
            capo_dataexchange.types.import_asset_from_api_gateway_api_response_details.deserialize_json(
                data["ImportAssetFromApiGatewayApi"]
            )
        )
    if "CreateS3DataAccessFromS3Bucket" in data:
        import capo_dataexchange.types.create_s3_data_access_from_s3_bucket_response_details

        out["create_s3_data_access_from_s3_bucket"] = (
            capo_dataexchange.types.create_s3_data_access_from_s3_bucket_response_details.deserialize_json(
                data["CreateS3DataAccessFromS3Bucket"]
            )
        )
    if "ImportAssetsFromLakeFormationTagPolicy" in data:
        import capo_dataexchange.types.import_assets_from_lake_formation_tag_policy_response_details

        out["import_assets_from_lake_formation_tag_policy"] = (
            capo_dataexchange.types.import_assets_from_lake_formation_tag_policy_response_details.deserialize_json(
                data["ImportAssetsFromLakeFormationTagPolicy"]
            )
        )
    return out
