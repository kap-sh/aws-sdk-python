"""Generated from Smithy shape ``com.amazonaws.apigateway#DomainNameStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

DomainNameStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UPDATING",
    "PENDING",
    "PENDING_CERTIFICATE_REIMPORT",
    "PENDING_OWNERSHIP_VERIFICATION",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UPDATING",
        "PENDING",
        "PENDING_CERTIFICATE_REIMPORT",
        "PENDING_OWNERSHIP_VERIFICATION",
        "FAILED",
    )
)


def serialize_json(value: DomainNameStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainNameStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainNameStatus value: {data!r}")
    return cast(DomainNameStatus, data)
