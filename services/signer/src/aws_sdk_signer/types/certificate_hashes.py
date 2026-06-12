"""Generated from Smithy shape ``com.amazonaws.signer#CertificateHashes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signer.types.string

CertificateHashes: TypeAlias = list["aws_sdk_signer.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateHashes) -> list:
    return list(value)


def deserialize_json(data: list) -> CertificateHashes:
    return list(data)
