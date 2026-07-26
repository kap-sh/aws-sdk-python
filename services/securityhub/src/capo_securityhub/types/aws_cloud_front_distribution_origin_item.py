"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_custom_origin_config
    import capo_securityhub.types.aws_cloud_front_distribution_origin_s3_origin_config
    import capo_securityhub.types.non_empty_string


class AwsCloudFrontDistributionOriginItem(TypedDict, closed=True):
    domain_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Amazon S3 origins: The DNS name of the S3 bucket from which you want CloudFront to get objects for this origin.</p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A unique identifier for the origin or origin group.</p>"""
    origin_path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin.</p>"""
    s3_origin_config: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origin_s3_origin_config.AwsCloudFrontDistributionOriginS3OriginConfig"
    ]
    """<p>An origin that is an S3 bucket that is not configured with static website hosting.</p>"""
    custom_origin_config: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origin_custom_origin_config.AwsCloudFrontDistributionOriginCustomOriginConfig"
    ]
    """<p>An origin that is not an Amazon S3 bucket, with one exception. If the Amazon S3 bucket is configured with static website hosting, use this attribute. If the Amazon S3 bucket is not configured with static website hosting, use the <code>S3OriginConfig</code> type instead. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginItem) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "origin_path" in value:
        out["OriginPath"] = value["origin_path"]
    if "s3_origin_config" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_s3_origin_config

        out["S3OriginConfig"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_s3_origin_config.serialize_json(
                value["s3_origin_config"]
            )
        )
    if "custom_origin_config" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_custom_origin_config

        out["CustomOriginConfig"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_custom_origin_config.serialize_json(
                value["custom_origin_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginItem:
    out: AwsCloudFrontDistributionOriginItem = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "OriginPath" in data:
        out["origin_path"] = data["OriginPath"]
    if "S3OriginConfig" in data:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_s3_origin_config

        out["s3_origin_config"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_s3_origin_config.deserialize_json(
                data["S3OriginConfig"]
            )
        )
    if "CustomOriginConfig" in data:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_custom_origin_config

        out["custom_origin_config"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_custom_origin_config.deserialize_json(
                data["CustomOriginConfig"]
            )
        )
    return out
