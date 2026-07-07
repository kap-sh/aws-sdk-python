"""Generated from Smithy shape ``com.amazonaws.emr#SessionManagedLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.xml_string


class SessionManagedLoggingConfiguration(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Whether Amazon EMR-managed logging is enabled for the session.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the managed logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionManagedLoggingConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionManagedLoggingConfiguration:
    out: SessionManagedLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    return out
