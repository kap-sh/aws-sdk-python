"""Generated from Smithy shape ``com.amazonaws.glue#DataCatalogEncryptionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_password_encryption
    import capo_glue.types.encryption_at_rest


class DataCatalogEncryptionSettings(TypedDict, closed=True):
    encryption_at_rest: NotRequired[
        "capo_glue.types.encryption_at_rest.EncryptionAtRest"
    ]
    """<p>Specifies the encryption-at-rest configuration for the Data Catalog.</p>"""
    connection_password_encryption: NotRequired[
        "capo_glue.types.connection_password_encryption.ConnectionPasswordEncryption"
    ]
    """<p>When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of <code>CreateConnection</code> or <code>UpdateConnection</code> and store it in the <code>ENCRYPTED_PASSWORD</code> field in the connection properties. You can enable catalog encryption or only password encryption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCatalogEncryptionSettings) -> dict:
    out: dict = {}
    if "encryption_at_rest" in value:
        import capo_glue.types.encryption_at_rest

        out["EncryptionAtRest"] = (
            capo_glue.types.encryption_at_rest.serialize_aws_json_1_1(
                value["encryption_at_rest"]
            )
        )
    if "connection_password_encryption" in value:
        import capo_glue.types.connection_password_encryption

        out["ConnectionPasswordEncryption"] = (
            capo_glue.types.connection_password_encryption.serialize_aws_json_1_1(
                value["connection_password_encryption"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataCatalogEncryptionSettings:
    out: DataCatalogEncryptionSettings = {}  # type: ignore[typeddict-item]
    if "EncryptionAtRest" in data:
        import capo_glue.types.encryption_at_rest

        out["encryption_at_rest"] = (
            capo_glue.types.encryption_at_rest.deserialize_aws_json_1_1(
                data["EncryptionAtRest"]
            )
        )
    if "ConnectionPasswordEncryption" in data:
        import capo_glue.types.connection_password_encryption

        out["connection_password_encryption"] = (
            capo_glue.types.connection_password_encryption.deserialize_aws_json_1_1(
                data["ConnectionPasswordEncryption"]
            )
        )
    return out
