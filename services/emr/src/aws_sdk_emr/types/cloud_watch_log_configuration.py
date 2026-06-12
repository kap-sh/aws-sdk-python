"""Generated from Smithy shape ``com.amazonaws.emr#CloudWatchLogConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.log_types_map
    import aws_sdk_emr.types.xml_string


class CloudWatchLogConfiguration(TypedDict):
    enabled: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Specifies if CloudWatch logging is enabled.</p>"""
    log_group_name: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name of the CloudWatch log group where logs are published.</p>"""
    log_stream_name_prefix: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The prefix of the log stream name.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The ARN of the encryption key used to encrypt the logs.</p>"""
    log_types: NotRequired["aws_sdk_emr.types.log_types_map.LogTypesMap"]
    """<p>A map of log types to file names for publishing logs to the standard output or standard error streams for CloudWatch. Valid log types include STEP_LOGS, SPARK_DRIVER, and SPARK_EXECUTOR. Valid file names for each type include STDOUT and STDERR.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLogConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "log_stream_name_prefix" in value:
        out["LogStreamNamePrefix"] = value["log_stream_name_prefix"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "log_types" in value:
        import aws_sdk_emr.types.log_types_map

        out["LogTypes"] = aws_sdk_emr.types.log_types_map.serialize_aws_json_1_1(
            value["log_types"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLogConfiguration:
    out: CloudWatchLogConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "LogGroupName" in data:
        out["log_group_name"] = data["LogGroupName"]
    if "LogStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["LogStreamNamePrefix"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "LogTypes" in data:
        import aws_sdk_emr.types.log_types_map

        out["log_types"] = aws_sdk_emr.types.log_types_map.deserialize_aws_json_1_1(
            data["LogTypes"]
        )
    return out
