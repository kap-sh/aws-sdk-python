"""Generated from Smithy shape ``com.amazonaws.iot#DomainType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DomainType: TypeAlias = Literal[
    "ENDPOINT",
    "AWS_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENDPOINT",
        "AWS_MANAGED",
        "CUSTOMER_MANAGED",
    )
)


def serialize_json(value: DomainType) -> str:
    return value


def deserialize_json(data: str) -> DomainType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainType value: {data!r}")
    return cast(DomainType, data)
