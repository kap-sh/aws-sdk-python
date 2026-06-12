"""Generated from Smithy shape ``com.amazonaws.amplify#DomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

DomainStatus: TypeAlias = Literal[
    "PENDING_VERIFICATION",
    "IN_PROGRESS",
    "AVAILABLE",
    "IMPORTING_CUSTOM_CERTIFICATE",
    "PENDING_DEPLOYMENT",
    "AWAITING_APP_CNAME",
    "FAILED",
    "CREATING",
    "REQUESTING_CERTIFICATE",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VERIFICATION",
        "IN_PROGRESS",
        "AVAILABLE",
        "IMPORTING_CUSTOM_CERTIFICATE",
        "PENDING_DEPLOYMENT",
        "AWAITING_APP_CNAME",
        "FAILED",
        "CREATING",
        "REQUESTING_CERTIFICATE",
        "UPDATING",
    )
)


def serialize_json(value: DomainStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainStatus value: {data!r}")
    return cast(DomainStatus, data)
