"""Generated from Smithy shape ``com.amazonaws.emrserverless#CloudWatchLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.encryption_key_arn
    import aws_sdk_emr_serverless.types.log_group_name
    import aws_sdk_emr_serverless.types.log_stream_name_prefix
    import aws_sdk_emr_serverless.types.log_type_map


class CloudWatchLoggingConfiguration(TypedDict, closed=True):
    enabled: "bool"
    """<p>Enables CloudWatch logging.</p>"""
    log_group_name: NotRequired[
        "aws_sdk_emr_serverless.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.</p>"""
    log_stream_name_prefix: NotRequired[
        "aws_sdk_emr_serverless.types.log_stream_name_prefix.LogStreamNamePrefix"
    ]
    """<p>Prefix for the CloudWatch log stream name.</p>"""
    encryption_key_arn: NotRequired[
        "aws_sdk_emr_serverless.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The Key Management Service (KMS) key ARN to encrypt the logs that you store in CloudWatch Logs.</p>"""
    log_types: NotRequired["aws_sdk_emr_serverless.types.log_type_map.LogTypeMap"]
    r"""<p>The types of logs that you want to publish to CloudWatch. If you don't specify any log types, driver STDOUT and STDERR logs will be published to CloudWatch Logs by default. For more information including the supported worker types for Hive and Spark, see <a href=\"https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging.html#jobs-log-storage-cw\">Logging for EMR Serverless with CloudWatch</a>.</p> <ul> <li> <p> <b>Key Valid Values</b>: <code>SPARK_DRIVER</code>, <code>SPARK_EXECUTOR</code>, <code>HIVE_DRIVER</code>, <code>TEZ_TASK</code> </p> </li> <li> <p> <b>Array Members Valid Values</b>: <code>STDOUT</code>, <code>STDERR</code>, <code>HIVE_LOG</code>, <code>TEZ_AM</code>, <code>SYSTEM_LOGS</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLoggingConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "log_types" in value:
        import aws_sdk_emr_serverless.types.log_type_map

        out["logTypes"] = aws_sdk_emr_serverless.types.log_type_map.serialize_json(
            value["log_types"]
        )
    return out


def deserialize_json(data: dict) -> CloudWatchLoggingConfiguration:
    out: CloudWatchLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("CloudWatchLoggingConfiguration.enabled required")
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "logStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "logTypes" in data:
        import aws_sdk_emr_serverless.types.log_type_map

        out["log_types"] = aws_sdk_emr_serverless.types.log_type_map.deserialize_json(
            data["logTypes"]
        )
    return out
