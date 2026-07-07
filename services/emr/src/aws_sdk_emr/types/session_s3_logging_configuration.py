"""Generated from Smithy shape ``com.amazonaws.emr#SessionS3LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.log_types_map
    import aws_sdk_emr.types.xml_string


class SessionS3LoggingConfiguration(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Whether Amazon S3 logging is enabled for the session.</p>"""
    log_uri: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Amazon S3 destination URI where session logs are published.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt logs published to Amazon S3.</p>"""
    log_types: NotRequired["aws_sdk_emr.types.log_types_map.LogTypesMap"]
    """<p>A map of log component names (for example, <code>SPARK_DRIVER</code>, <code>SPARK_EXECUTOR</code>) to the list of log types to publish for that component (for example, <code>stdout</code>, <code>stderr</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionS3LoggingConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "log_types" in value:
        import aws_sdk_emr.types.log_types_map

        out["LogTypes"] = aws_sdk_emr.types.log_types_map.serialize_aws_json_1_1(
            value["log_types"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionS3LoggingConfiguration:
    out: SessionS3LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "LogUri" in data:
        out["log_uri"] = data["LogUri"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "LogTypes" in data:
        import aws_sdk_emr.types.log_types_map

        out["log_types"] = aws_sdk_emr.types.log_types_map.deserialize_aws_json_1_1(
            data["LogTypes"]
        )
    return out
