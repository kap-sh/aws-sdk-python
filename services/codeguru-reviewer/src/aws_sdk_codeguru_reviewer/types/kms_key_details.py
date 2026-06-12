"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#KMSKeyDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.encryption_option
    import aws_sdk_codeguru_reviewer.types.kms_key_id


class KMSKeyDetails(TypedDict):
    kms_key_id: NotRequired["aws_sdk_codeguru_reviewer.types.kms_key_id.KMSKeyId"]
    """<p>The ID of the Amazon Web Services KMS key that is associated with a repository association.</p>"""
    encryption_option: NotRequired[
        "aws_sdk_codeguru_reviewer.types.encryption_option.EncryptionOption"
    ]
    """<p>The encryption option for a repository association. It is either owned by Amazon Web Services Key Management Service (KMS) (<code>AWS_OWNED_CMK</code>) or customer managed (<code>CUSTOMER_MANAGED_CMK</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KMSKeyDetails) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    if "encryption_option" in value:
        import aws_sdk_codeguru_reviewer.types.encryption_option

        out["EncryptionOption"] = (
            aws_sdk_codeguru_reviewer.types.encryption_option.serialize_json(
                value["encryption_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> KMSKeyDetails:
    out: KMSKeyDetails = {}  # type: ignore[typeddict-item]
    if "KMSKeyId" in data:
        out["kms_key_id"] = data["KMSKeyId"]
    if "EncryptionOption" in data:
        import aws_sdk_codeguru_reviewer.types.encryption_option

        out["encryption_option"] = (
            aws_sdk_codeguru_reviewer.types.encryption_option.deserialize_json(
                data["EncryptionOption"]
            )
        )
    return out
