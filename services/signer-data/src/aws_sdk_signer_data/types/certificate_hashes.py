"""Generated from Smithy shape ``com.amazonaws.signerdata#CertificateHashes``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_signer_data.types.certificate_hash

CertificateHashes: TypeAlias = list["aws_sdk_signer_data.types.certificate_hash.CertificateHash"]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateHashes) -> list:
    return list(value)


def deserialize_json(data: list) -> CertificateHashes:
    return list(data)