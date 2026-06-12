"""Generated from Smithy shape ``com.amazonaws.emr#S3MonitoringConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string


class S3MonitoringConfiguration(TypedDict):
    log_uri: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Amazon S3 destination URI for log publishing.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3MonitoringConfiguration) -> dict:
    out: dict = {}
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3MonitoringConfiguration:
    out: S3MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "LogUri" in data:
        out["log_uri"] = data["LogUri"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    return out
