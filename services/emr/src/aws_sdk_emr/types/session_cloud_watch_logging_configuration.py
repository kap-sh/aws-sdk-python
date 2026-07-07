"""Generated from Smithy shape ``com.amazonaws.emr#SessionCloudWatchLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.log_types_map
    import aws_sdk_emr.types.xml_string


class SessionCloudWatchLoggingConfiguration(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Whether CloudWatch Logs is enabled for the session.</p>"""
    log_group: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name of the log group where session logs are published.</p>"""
    log_stream_name_prefix: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The prefix applied to the log stream name where session logs are published.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the logs published to CloudWatch Logs.</p>"""
    log_types: NotRequired["aws_sdk_emr.types.log_types_map.LogTypesMap"]
    """<p>A map of log component names (for example, <code>SPARK_DRIVER</code>, <code>SPARK_EXECUTOR</code>) to the list of log types to publish for that component (for example, <code>stdout</code>, <code>stderr</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionCloudWatchLoggingConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
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


def deserialize_aws_json_1_1(data: dict) -> SessionCloudWatchLoggingConfiguration:
    out: SessionCloudWatchLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
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
