"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

IntegrationStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
    )
)


def serialize_json(value: IntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> IntegrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationStatus value: {data!r}")
    return cast(IntegrationStatus, data)
