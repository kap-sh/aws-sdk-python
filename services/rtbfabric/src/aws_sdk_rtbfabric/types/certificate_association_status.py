"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CertificateAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

"""<p>The status of a certificate association with a gateway.</p>"""
CertificateAssociationStatus: TypeAlias = Literal[
    "PENDING_ASSOCIATION",
    "ASSOCIATED",
    "PENDING_DISASSOCIATION",
    "DISASSOCIATED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_ASSOCIATION",
        "ASSOCIATED",
        "PENDING_DISASSOCIATION",
        "DISASSOCIATED",
        "FAILED",
    )
)


def serialize_json(value: CertificateAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> CertificateAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateAssociationStatus value: {data!r}"
        )
    return cast(CertificateAssociationStatus, data)
