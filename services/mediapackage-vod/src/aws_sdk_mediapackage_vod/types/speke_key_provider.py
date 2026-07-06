"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#SpekeKeyProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__list_of__string
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.encryption_contract_configuration


class SpekeKeyProvider(TypedDict, closed=True):
    encryption_contract_configuration: NotRequired[
        "aws_sdk_mediapackage_vod.types.encryption_contract_configuration.EncryptionContractConfiguration"
    ]
    role_arn: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service."""
    system_ids: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of__string.__listOf__string"
    ]
    """The system IDs to include in key requests."""
    url: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The URL of the external key provider service."""


# --- restJson1 ser/de ---
def serialize_json(value: SpekeKeyProvider) -> dict:
    out: dict = {}
    if "encryption_contract_configuration" in value:
        import aws_sdk_mediapackage_vod.types.encryption_contract_configuration

        out["encryptionContractConfiguration"] = (
            aws_sdk_mediapackage_vod.types.encryption_contract_configuration.serialize_json(
                value["encryption_contract_configuration"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "system_ids" in value:
        import aws_sdk_mediapackage_vod.types.__list_of__string

        out["systemIds"] = (
            aws_sdk_mediapackage_vod.types.__list_of__string.serialize_json(
                value["system_ids"]
            )
        )
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SpekeKeyProvider:
    out: SpekeKeyProvider = {}  # type: ignore[typeddict-item]
    if "encryptionContractConfiguration" in data:
        import aws_sdk_mediapackage_vod.types.encryption_contract_configuration

        out["encryption_contract_configuration"] = (
            aws_sdk_mediapackage_vod.types.encryption_contract_configuration.deserialize_json(
                data["encryptionContractConfiguration"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "systemIds" in data:
        import aws_sdk_mediapackage_vod.types.__list_of__string

        out["system_ids"] = (
            aws_sdk_mediapackage_vod.types.__list_of__string.deserialize_json(
                data["systemIds"]
            )
        )
    if "url" in data:
        out["url"] = data["url"]
    return out
