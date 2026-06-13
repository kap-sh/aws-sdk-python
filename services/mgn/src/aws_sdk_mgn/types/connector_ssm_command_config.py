"""Generated from Smithy shape ``com.amazonaws.mgn#ConnectorSsmCommandConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.cloud_watch_log_group_name
    import aws_sdk_mgn.types.s3_bucket_name


class ConnectorSsmCommandConfig(TypedDict):
    s3_output_enabled: "bool"
    """<p>Connector SSM command config S3 output enabled.</p>"""
    output_s3_bucket_name: NotRequired["aws_sdk_mgn.types.s3_bucket_name.S3BucketName"]
    """<p>Connector SSM command config output S3 bucket name.</p>"""
    cloud_watch_output_enabled: "bool"
    """<p>Connector SSM command config CloudWatch output enabled.</p>"""
    cloud_watch_log_group_name: NotRequired[
        "aws_sdk_mgn.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>Connector SSM command config CloudWatch log group name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSsmCommandConfig) -> dict:
    out: dict = {}
    out["s3OutputEnabled"] = value["s3_output_enabled"]
    if "output_s3_bucket_name" in value:
        out["outputS3BucketName"] = value["output_s3_bucket_name"]
    out["cloudWatchOutputEnabled"] = value["cloud_watch_output_enabled"]
    if "cloud_watch_log_group_name" in value:
        out["cloudWatchLogGroupName"] = value["cloud_watch_log_group_name"]
    return out


def deserialize_json(data: dict) -> ConnectorSsmCommandConfig:
    out: ConnectorSsmCommandConfig = {}  # type: ignore[typeddict-item]
    if "s3OutputEnabled" in data:
        out["s3_output_enabled"] = data["s3OutputEnabled"]
    else:
        raise DeserializationError(
            "ConnectorSsmCommandConfig.s3_output_enabled required"
        )
    if "outputS3BucketName" in data:
        out["output_s3_bucket_name"] = data["outputS3BucketName"]
    if "cloudWatchOutputEnabled" in data:
        out["cloud_watch_output_enabled"] = data["cloudWatchOutputEnabled"]
    else:
        raise DeserializationError(
            "ConnectorSsmCommandConfig.cloud_watch_output_enabled required"
        )
    if "cloudWatchLogGroupName" in data:
        out["cloud_watch_log_group_name"] = data["cloudWatchLogGroupName"]
    return out
