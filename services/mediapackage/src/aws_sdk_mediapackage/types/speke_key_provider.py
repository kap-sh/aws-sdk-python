"""Generated from Smithy shape ``com.amazonaws.mediapackage#SpekeKeyProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__list_of__string
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.encryption_contract_configuration


class SpekeKeyProvider(TypedDict, closed=True):
    certificate_arn: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service."""
    encryption_contract_configuration: NotRequired[
        "aws_sdk_mediapackage.types.encryption_contract_configuration.EncryptionContractConfiguration"
    ]
    resource_id: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The resource ID to include in key requests."""
    role_arn: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service."""
    system_ids: NotRequired[
        "aws_sdk_mediapackage.types.__list_of__string.__listOf__string"
    ]
    """The system IDs to include in key requests."""
    url: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The URL of the external key provider service."""


# --- restJson1 ser/de ---
def serialize_json(value: SpekeKeyProvider) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "encryption_contract_configuration" in value:
        import aws_sdk_mediapackage.types.encryption_contract_configuration

        out["encryptionContractConfiguration"] = (
            aws_sdk_mediapackage.types.encryption_contract_configuration.serialize_json(
                value["encryption_contract_configuration"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "system_ids" in value:
        import aws_sdk_mediapackage.types.__list_of__string

        out["systemIds"] = aws_sdk_mediapackage.types.__list_of__string.serialize_json(
            value["system_ids"]
        )
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SpekeKeyProvider:
    out: SpekeKeyProvider = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "encryptionContractConfiguration" in data:
        import aws_sdk_mediapackage.types.encryption_contract_configuration

        out["encryption_contract_configuration"] = (
            aws_sdk_mediapackage.types.encryption_contract_configuration.deserialize_json(
                data["encryptionContractConfiguration"]
            )
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "systemIds" in data:
        import aws_sdk_mediapackage.types.__list_of__string

        out["system_ids"] = (
            aws_sdk_mediapackage.types.__list_of__string.deserialize_json(
                data["systemIds"]
            )
        )
    if "url" in data:
        out["url"] = data["url"]
    return out
