"""Generated from Smithy shape ``com.amazonaws.securityagent#DomainVerificationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Method used to verify domain ownership.</p>"""
DomainVerificationMethod: TypeAlias = Literal[
    "DNS_TXT",
    "HTTP_ROUTE",
    "PRIVATE_VPC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DNS_TXT",
        "HTTP_ROUTE",
        "PRIVATE_VPC",
    )
)


def serialize_json(value: DomainVerificationMethod) -> str:
    return value


def deserialize_json(data: str) -> DomainVerificationMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainVerificationMethod value: {data!r}")
    return cast(DomainVerificationMethod, data)
