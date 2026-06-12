"""Generated from Smithy shape ``com.amazonaws.bedrock#CloudWatchConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.log_group_name
    import aws_sdk_bedrock.types.role_arn
    import aws_sdk_bedrock.types.s3_config


class CloudWatchConfig(TypedDict):
    log_group_name: "aws_sdk_bedrock.types.log_group_name.LogGroupName"
    """<p>The log group name.</p>"""
    role_arn: "aws_sdk_bedrock.types.role_arn.RoleArn"
    """<p>The role Amazon Resource Name (ARN).</p>"""
    large_data_delivery_s3_config: NotRequired[
        "aws_sdk_bedrock.types.s3_config.S3Config"
    ]
    """<p>S3 configuration for delivering a large amount of data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchConfig) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["roleArn"] = value["role_arn"]
    if "large_data_delivery_s3_config" in value:
        import aws_sdk_bedrock.types.s3_config

        out["largeDataDeliveryS3Config"] = (
            aws_sdk_bedrock.types.s3_config.serialize_json(
                value["large_data_delivery_s3_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchConfig:
    out: CloudWatchConfig = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("CloudWatchConfig.log_group_name required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CloudWatchConfig.role_arn required")
    if "largeDataDeliveryS3Config" in data:
        import aws_sdk_bedrock.types.s3_config

        out["large_data_delivery_s3_config"] = (
            aws_sdk_bedrock.types.s3_config.deserialize_json(
                data["largeDataDeliveryS3Config"]
            )
        )
    return out
