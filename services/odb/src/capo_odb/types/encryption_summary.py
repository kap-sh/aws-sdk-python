"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.encryption_key_configuration
    import capo_odb.types.encryption_key_provider


class EncryptionSummary(TypedDict, closed=True):
    encryption_key_provider: NotRequired[
        "capo_odb.types.encryption_key_provider.EncryptionKeyProvider"
    ]
    """<p>The provider of the encryption key used for the Autonomous Database.</p>"""
    encryption_key_configuration: NotRequired[
        "capo_odb.types.encryption_key_configuration.EncryptionKeyConfiguration"
    ]
    """<p>The configuration of the encryption key used for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionSummary) -> dict:
    out: dict = {}
    if "encryption_key_provider" in value:
        import capo_odb.types.encryption_key_provider

        out["encryptionKeyProvider"] = (
            capo_odb.types.encryption_key_provider.serialize_aws_json_1_0(
                value["encryption_key_provider"]
            )
        )
    if "encryption_key_configuration" in value:
        import capo_odb.types.encryption_key_configuration

        out["encryptionKeyConfiguration"] = (
            capo_odb.types.encryption_key_configuration.serialize_aws_json_1_0(
                value["encryption_key_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionSummary:
    out: EncryptionSummary = {}  # type: ignore[typeddict-item]
    if "encryptionKeyProvider" in data:
        import capo_odb.types.encryption_key_provider

        out["encryption_key_provider"] = (
            capo_odb.types.encryption_key_provider.deserialize_aws_json_1_0(
                data["encryptionKeyProvider"]
            )
        )
    if "encryptionKeyConfiguration" in data:
        import capo_odb.types.encryption_key_configuration

        out["encryption_key_configuration"] = (
            capo_odb.types.encryption_key_configuration.deserialize_aws_json_1_0(
                data["encryptionKeyConfiguration"]
            )
        )
    return out
