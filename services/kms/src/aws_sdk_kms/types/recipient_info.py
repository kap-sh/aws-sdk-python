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
