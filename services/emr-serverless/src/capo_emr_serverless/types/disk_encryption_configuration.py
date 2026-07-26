"""Generated from Smithy shape ``com.amazonaws.emrserverless#DiskEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.encryption_context
    import capo_emr_serverless.types.encryption_key_arn


class DiskEncryptionConfiguration(TypedDict, closed=True):
    encryption_context: NotRequired[
        "capo_emr_serverless.types.encryption_context.EncryptionContext"
    ]
    """<p>Specifies the optional encryption context that will be used when encrypting the data. An encryption context is a collection of non-secret key-value pairs that represent additional authenticated data. </p>"""
    encryption_key_arn: NotRequired[
        "capo_emr_serverless.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The KMS key ARN to encrypt local disks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiskEncryptionConfiguration) -> dict:
    out: dict = {}
    if "encryption_context" in value:
        import capo_emr_serverless.types.encryption_context

        out["encryptionContext"] = (
            capo_emr_serverless.types.encryption_context.serialize_json(
                value["encryption_context"]
            )
        )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> DiskEncryptionConfiguration:
    out: DiskEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "encryptionContext" in data:
        import capo_emr_serverless.types.encryption_context

        out["encryption_context"] = (
            capo_emr_serverless.types.encryption_context.deserialize_json(
                data["encryptionContext"]
            )
        )
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
