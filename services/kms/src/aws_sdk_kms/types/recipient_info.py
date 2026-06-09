"""Generated from Smithy shape ``com.amazonaws.kms#RecipientInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.attestation_document_type
    import aws_sdk_kms.types.key_encryption_mechanism


class RecipientInfo(TypedDict):
    key_encryption_algorithm: NotRequired[
        "aws_sdk_kms.types.key_encryption_mechanism.KeyEncryptionMechanism"
    ]
    """<p>The encryption algorithm that KMS should use with the public key for an Amazon Web Services Nitro Enclave or NitroTPM to encrypt plaintext values for the response. The only valid value is <code>RSAES_OAEP_SHA_256</code>.</p>"""
    attestation_document: NotRequired[
        "aws_sdk_kms.types.attestation_document_type.AttestationDocumentType"
    ]
    """<p>The attestation document for an Amazon Web Services Nitro Enclave or a NitroTPM. This document includes the enclave's public key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecipientInfo) -> dict:
    out: dict = {}
    if "key_encryption_algorithm" in value:
        import aws_sdk_kms.types.key_encryption_mechanism

        out["KeyEncryptionAlgorithm"] = (
            aws_sdk_kms.types.key_encryption_mechanism.serialize_aws_json_1_1(
                value["key_encryption_algorithm"]
            )
        )
    if "attestation_document" in value:
        import aws_sdk_kms.types.attestation_document_type

        out["AttestationDocument"] = (
            aws_sdk_kms.types.attestation_document_type.serialize_aws_json_1_1(
                value["attestation_document"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecipientInfo:
    out: RecipientInfo = {}  # type: ignore[typeddict-item]
    if "KeyEncryptionAlgorithm" in data:
        import aws_sdk_kms.types.key_encryption_mechanism

        out["key_encryption_algorithm"] = (
            aws_sdk_kms.types.key_encryption_mechanism.deserialize_aws_json_1_1(
                data["KeyEncryptionAlgorithm"]
            )
        )
    if "AttestationDocument" in data:
        import aws_sdk_kms.types.attestation_document_type

        out["attestation_document"] = (
            aws_sdk_kms.types.attestation_document_type.deserialize_aws_json_1_1(
                data["AttestationDocument"]
            )
        )
    return out
