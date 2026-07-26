"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3AccessPointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_access_point_vpc_configuration_details
    import capo_securityhub.types.aws_s3_account_public_access_block_details
    import capo_securityhub.types.non_empty_string


class AwsS3AccessPointDetails(TypedDict, closed=True):
    access_point_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the access point. </p>"""
    alias: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name or alias of the access point. </p>"""
    bucket: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the S3 bucket associated with the specified access point. </p>"""
    bucket_account_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Web Services account ID associated with the S3 bucket associated with this access point. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the specified access point. </p>"""
    network_origin: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates whether this access point allows access from the public internet. </p>"""
    public_access_block_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_account_public_access_block_details.AwsS3AccountPublicAccessBlockDetails"
    ]
    vpc_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_access_point_vpc_configuration_details.AwsS3AccessPointVpcConfigurationDetails"
    ]
    """<p> Contains the virtual private cloud (VPC) configuration for the specified access point. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3AccessPointDetails) -> dict:
    out: dict = {}
    if "access_point_arn" in value:
        out["AccessPointArn"] = value["access_point_arn"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "bucket_account_id" in value:
        out["BucketAccountId"] = value["bucket_account_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "network_origin" in value:
        out["NetworkOrigin"] = value["network_origin"]
    if "public_access_block_configuration" in value:
        import capo_securityhub.types.aws_s3_account_public_access_block_details

        out["PublicAccessBlockConfiguration"] = (
            capo_securityhub.types.aws_s3_account_public_access_block_details.serialize_json(
                value["public_access_block_configuration"]
            )
        )
    if "vpc_configuration" in value:
        import capo_securityhub.types.aws_s3_access_point_vpc_configuration_details

        out["VpcConfiguration"] = (
            capo_securityhub.types.aws_s3_access_point_vpc_configuration_details.serialize_json(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3AccessPointDetails:
    out: AwsS3AccessPointDetails = {}  # type: ignore[typeddict-item]
    if "AccessPointArn" in data:
        out["access_point_arn"] = data["AccessPointArn"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "BucketAccountId" in data:
        out["bucket_account_id"] = data["BucketAccountId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "NetworkOrigin" in data:
        out["network_origin"] = data["NetworkOrigin"]
    if "PublicAccessBlockConfiguration" in data:
        import capo_securityhub.types.aws_s3_account_public_access_block_details

        out["public_access_block_configuration"] = (
            capo_securityhub.types.aws_s3_account_public_access_block_details.deserialize_json(
                data["PublicAccessBlockConfiguration"]
            )
        )
    if "VpcConfiguration" in data:
        import capo_securityhub.types.aws_s3_access_point_vpc_configuration_details

        out["vpc_configuration"] = (
            capo_securityhub.types.aws_s3_access_point_vpc_configuration_details.deserialize_json(
                data["VpcConfiguration"]
            )
        )
    return out
