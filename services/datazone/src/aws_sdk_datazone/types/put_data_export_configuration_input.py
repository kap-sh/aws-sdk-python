"""Generated from Smithy shape ``com.amazonaws.datazone#PutDataExportConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.encryption_configuration


class PutDataExportConfigurationInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The domain ID for which you want to create data export configuration details.</p>"""
    enable_export: "bool"
    """<p>Specifies that the export is to be enabled as part of creating data export configuration details.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_datazone.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration as part of creating data export configuration details.</p> <p>The KMS key provided here as part of encryptionConfiguration must have the required permissions as described in <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.html\">KMS permissions for exporting asset metadata in Amazon SageMaker Unified Studio</a>.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDataExportConfigurationInput) -> dict:
    out: dict = {}
    out["enableExport"] = value["enable_export"]
    if "encryption_configuration" in value:
        import aws_sdk_datazone.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_datazone.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutDataExportConfigurationInput:
    out: PutDataExportConfigurationInput = {}  # type: ignore[typeddict-item]
    if "enableExport" in data:
        out["enable_export"] = data["enableExport"]
    else:
        raise DeserializationError(
            "PutDataExportConfigurationInput.enable_export required"
        )
    if "encryptionConfiguration" in data:
        import aws_sdk_datazone.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_datazone.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
