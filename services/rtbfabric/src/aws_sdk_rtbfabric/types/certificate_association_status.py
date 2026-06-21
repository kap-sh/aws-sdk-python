"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CertificateAssociationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a certificate association with a gateway.</p>"""
CertificateAssociationStatus: TypeAlias = Literal[
    "PENDING_ASSOCIATION",
    "ASSOCIATED",
    "PENDING_DISASSOCIATION",
    "DISASSOCIATED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> CertificateAssociationStatus:
    return cast(CertificateAssociationStatus, data)
