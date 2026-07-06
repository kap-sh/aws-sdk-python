"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationS3Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn_list
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.location_uri
    import aws_sdk_datasync.types.s3_config
    import aws_sdk_datasync.types.s3_storage_class
    import aws_sdk_datasync.types.time


class DescribeLocationS3Response(TypedDict, closed=True):
    location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the Amazon S3 location.</p>"""
    location_uri: NotRequired["aws_sdk_datasync.types.location_uri.LocationUri"]
    """<p>The URL of the Amazon S3 location that was described.</p>"""
    s3_storage_class: NotRequired[
        "aws_sdk_datasync.types.s3_storage_class.S3StorageClass"
    ]
    r"""<p>When Amazon S3 is a destination location, this is the storage class that you chose for your objects.</p> <p>Some storage classes have behaviors that can affect your Amazon S3 storage costs. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes\">Storage class considerations with Amazon S3 transfers</a>.</p>"""
    s3_config: NotRequired["aws_sdk_datasync.types.s3_config.S3Config"]
    agent_arns: NotRequired["aws_sdk_datasync.types.agent_arn_list.AgentArnList"]
    r"""<p>The ARNs of the DataSync agents deployed on your Outpost when using working with Amazon S3 on Outposts.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/deploy-agents.html#outposts-agent\">Deploy your DataSync agent on Outposts</a>.</p>"""
    creation_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the Amazon S3 location was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationS3Response) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "s3_storage_class" in value:
        import aws_sdk_datasync.types.s3_storage_class

        out["S3StorageClass"] = (
            aws_sdk_datasync.types.s3_storage_class.serialize_aws_json_1_1(
                value["s3_storage_class"]
            )
        )
    if "s3_config" in value:
        import aws_sdk_datasync.types.s3_config

        out["S3Config"] = aws_sdk_datasync.types.s3_config.serialize_aws_json_1_1(
            value["s3_config"]
        )
    if "agent_arns" in value:
        import aws_sdk_datasync.types.agent_arn_list

        out["AgentArns"] = aws_sdk_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "creation_time" in value:
        import aws_sdk_datasync.types.time

        out["CreationTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationS3Response:
    out: DescribeLocationS3Response = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "S3StorageClass" in data:
        import aws_sdk_datasync.types.s3_storage_class

        out["s3_storage_class"] = (
            aws_sdk_datasync.types.s3_storage_class.deserialize_aws_json_1_1(
                data["S3StorageClass"]
            )
        )
    if "S3Config" in data:
        import aws_sdk_datasync.types.s3_config

        out["s3_config"] = aws_sdk_datasync.types.s3_config.deserialize_aws_json_1_1(
            data["S3Config"]
        )
    if "AgentArns" in data:
        import aws_sdk_datasync.types.agent_arn_list

        out["agent_arns"] = (
            aws_sdk_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
                data["AgentArns"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_datasync.types.time

        out["creation_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
