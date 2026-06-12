"""Generated from Smithy shape ``com.amazonaws.dataexchange#RequestDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.create_s3_data_access_from_s3_bucket_request_details
    import aws_sdk_dataexchange.types.export_asset_to_signed_url_request_details
    import aws_sdk_dataexchange.types.export_assets_to_s3_request_details
    import aws_sdk_dataexchange.types.export_revisions_to_s3_request_details
    import aws_sdk_dataexchange.types.import_asset_from_api_gateway_api_request_details
    import aws_sdk_dataexchange.types.import_asset_from_signed_url_request_details
    import aws_sdk_dataexchange.types.import_assets_from_lake_formation_tag_policy_request_details
    import aws_sdk_dataexchange.types.import_assets_from_redshift_data_shares_request_details
    import aws_sdk_dataexchange.types.import_assets_from_s3_request_details


class RequestDetails(TypedDict):
    export_asset_to_signed_url: NotRequired[
        "aws_sdk_dataexchange.types.export_asset_to_signed_url_request_details.ExportAssetToSignedUrlRequestDetails"
    ]
    """<p>Details about the export to signed URL request.</p>"""
    export_assets_to_s3: NotRequired[
        "aws_sdk_dataexchange.types.export_assets_to_s3_request_details.ExportAssetsToS3RequestDetails"
    ]
    """<p>Details about the export to Amazon S3 request.</p>"""
    export_revisions_to_s3: NotRequired[
        "aws_sdk_dataexchange.types.export_revisions_to_s3_request_details.ExportRevisionsToS3RequestDetails"
    ]
    """<p>Details about the export to Amazon S3 request.</p>"""
    import_asset_from_signed_url: NotRequired[
        "aws_sdk_dataexchange.types.import_asset_from_signed_url_request_details.ImportAssetFromSignedUrlRequestDetails"
    ]
    """<p>Details about the import from Amazon S3 request.</p>"""
    import_assets_from_s3: NotRequired[
        "aws_sdk_dataexchange.types.import_assets_from_s3_request_details.ImportAssetsFromS3RequestDetails"
    ]
    """<p>Details about the import asset from API Gateway API request.</p>"""
    import_assets_from_redshift_data_shares: NotRequired[
        "aws_sdk_dataexchange.types.import_assets_from_redshift_data_shares_request_details.ImportAssetsFromRedshiftDataSharesRequestDetails"
    ]
    """<p>Details from an import from Amazon Redshift datashare request.</p>"""
    import_asset_from_api_gateway_api: NotRequired[
        "aws_sdk_dataexchange.types.import_asset_from_api_gateway_api_request_details.ImportAssetFromApiGatewayApiRequestDetails"
    ]
    """<p>Details about the import from signed URL request.</p>"""
    create_s3_data_access_from_s3_bucket: NotRequired[
        "aws_sdk_dataexchange.types.create_s3_data_access_from_s3_bucket_request_details.CreateS3DataAccessFromS3BucketRequestDetails"
    ]
    """<p>Details of the request to create S3 data access from the Amazon S3 bucket.</p>"""
    import_assets_from_lake_formation_tag_policy: NotRequired[
        "aws_sdk_dataexchange.types.import_assets_from_lake_formation_tag_policy_request_details.ImportAssetsFromLakeFormationTagPolicyRequestDetails"
    ]
    """<p>Request details for the ImportAssetsFromLakeFormationTagPolicy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestDetails) -> dict:
    out: dict = {}
    if "export_asset_to_signed_url" in value:
        import aws_sdk_dataexchange.types.export_asset_to_signed_url_request_details

        out["ExportAssetToSignedUrl"] = (
            aws_sdk_dataexchange.types.export_asset_to_signed_url_request_details.serialize_json(
                value["export_asset_to_signed_url"]
            )
        )
    if "export_assets_to_s3" in value:
        import aws_sdk_dataexchange.types.export_assets_to_s3_request_details

        out["ExportAssetsToS3"] = (
            aws_sdk_dataexchange.types.export_assets_to_s3_request_details.serialize_json(
                value["export_assets_to_s3"]
            )
        )
    if "export_revisions_to_s3" in value:
        import aws_sdk_dataexchange.types.export_revisions_to_s3_request_details

        out["ExportRevisionsToS3"] = (
            aws_sdk_dataexchange.types.export_revisions_to_s3_request_details.serialize_json(
                value["export_revisions_to_s3"]
            )
        )
    if "import_asset_from_signed_url" in value:
        import aws_sdk_dataexchange.types.import_asset_from_signed_url_request_details

        out["ImportAssetFromSignedUrl"] = (
            aws_sdk_dataexchange.types.import_asset_from_signed_url_request_details.serialize_json(
                value["import_asset_from_signed_url"]
            )
        )
    if "import_assets_from_s3" in value:
        import aws_sdk_dataexchange.types.import_assets_from_s3_request_details

        out["ImportAssetsFromS3"] = (
            aws_sdk_dataexchange.types.import_assets_from_s3_request_details.serialize_json(
                value["import_assets_from_s3"]
            )
        )
    if "import_assets_from_redshift_data_shares" in value:
        import aws_sdk_dataexchange.types.import_assets_from_redshift_data_shares_request_details

        out["ImportAssetsFromRedshiftDataShares"] = (
            aws_sdk_dataexchange.types.import_assets_from_redshift_data_shares_request_details.serialize_json(
                value["import_assets_from_redshift_data_shares"]
            )
        )
    if "import_asset_from_api_gateway_api" in value:
        import aws_sdk_dataexchange.types.import_asset_from_api_gateway_api_request_details

        out["ImportAssetFromApiGatewayApi"] = (
            aws_sdk_dataexchange.types.import_asset_from_api_gateway_api_request_details.serialize_json(
                value["import_asset_from_api_gateway_api"]
            )
        )
    if "create_s3_data_access_from_s3_bucket" in value:
        import aws_sdk_dataexchange.types.create_s3_data_access_from_s3_bucket_request_details

        out["CreateS3DataAccessFromS3Bucket"] = (
            aws_sdk_dataexchange.types.create_s3_data_access_from_s3_bucket_request_details.serialize_json(
                value["create_s3_data_access_from_s3_bucket"]
            )
        )
    if "import_assets_from_lake_formation_tag_policy" in value:
        import aws_sdk_dataexchange.types.import_assets_from_lake_formation_tag_policy_request_details

        out["ImportAssetsFromLakeFormationTagPolicy"] = (
            aws_sdk_dataexchange.types.import_assets_from_lake_formation_tag_policy_request_details.serialize_json(
                value["import_assets_from_lake_formation_tag_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> RequestDetails:
    out: RequestDetails = {}  # type: ignore[typeddict-item]
    if "ExportAssetToSignedUrl" in data:
        import aws_sdk_dataexchange.types.export_asset_to_signed_url_request_details

        out["export_asset_to_signed_url"] = (
            aws_sdk_dataexchange.types.export_asset_to_signed_url_request_details.deserialize_json(
                data["ExportAssetToSignedUrl"]
            )
        )
    if "ExportAssetsToS3" in data:
        import aws_sdk_dataexchange.types.export_assets_to_s3_request_details

        out["export_assets_to_s3"] = (
            aws_sdk_dataexchange.types.export_assets_to_s3_request_details.deserialize_json(
                data["ExportAssetsToS3"]
            )
        )
    if "ExportRevisionsToS3" in data:
        import aws_sdk_dataexchange.types.export_revisions_to_s3_request_details

        out["export_revisions_to_s3"] = (
            aws_sdk_dataexchange.types.export_revisions_to_s3_request_details.deserialize_json(
                data["ExportRevisionsToS3"]
            )
        )
    if "ImportAssetFromSignedUrl" in data:
        import aws_sdk_dataexchange.types.import_asset_from_signed_url_request_details

        out["import_asset_from_signed_url"] = (
            aws_sdk_dataexchange.types.import_asset_from_signed_url_request_details.deserialize_json(
                data["ImportAssetFromSignedUrl"]
            )
        )
    if "ImportAssetsFromS3" in data:
        import aws_sdk_dataexchange.types.import_assets_from_s3_request_details

        out["import_assets_from_s3"] = (
            aws_sdk_dataexchange.types.import_assets_from_s3_request_details.deserialize_json(
                data["ImportAssetsFromS3"]
            )
        )
    if "ImportAssetsFromRedshiftDataShares" in data:
        import aws_sdk_dataexchange.types.import_assets_from_redshift_data_shares_request_details

        out["import_assets_from_redshift_data_shares"] = (
            aws_sdk_dataexchange.types.import_assets_from_redshift_data_shares_request_details.deserialize_json(
                data["ImportAssetsFromRedshiftDataShares"]
            )
        )
    if "ImportAssetFromApiGatewayApi" in data:
        import aws_sdk_dataexchange.types.import_asset_from_api_gateway_api_request_details

        out["import_asset_from_api_gateway_api"] = (
            aws_sdk_dataexchange.types.import_asset_from_api_gateway_api_request_details.deserialize_json(
                data["ImportAssetFromApiGatewayApi"]
            )
        )
    if "CreateS3DataAccessFromS3Bucket" in data:
        import aws_sdk_dataexchange.types.create_s3_data_access_from_s3_bucket_request_details

        out["create_s3_data_access_from_s3_bucket"] = (
            aws_sdk_dataexchange.types.create_s3_data_access_from_s3_bucket_request_details.deserialize_json(
                data["CreateS3DataAccessFromS3Bucket"]
            )
        )
    if "ImportAssetsFromLakeFormationTagPolicy" in data:
        import aws_sdk_dataexchange.types.import_assets_from_lake_formation_tag_policy_request_details

        out["import_assets_from_lake_formation_tag_policy"] = (
            aws_sdk_dataexchange.types.import_assets_from_lake_formation_tag_policy_request_details.deserialize_json(
                data["ImportAssetsFromLakeFormationTagPolicy"]
            )
        )
    return out
