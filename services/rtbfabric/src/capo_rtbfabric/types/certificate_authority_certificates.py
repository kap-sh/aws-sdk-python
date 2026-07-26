"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CertificateAuthorityCertificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.base64_encoded_certificate_chain

CertificateAuthorityCertificates: TypeAlias = list[
    "capo_rtbfabric.types.base64_encoded_certificate_chain.Base64EncodedCertificateChain"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityCertificates) -> list:
    return list(value)


def deserialize_json(data: list) -> CertificateAuthorityCertificates:
    return list(data)
