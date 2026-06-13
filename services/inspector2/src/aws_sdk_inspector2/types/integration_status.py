"""Generated from Smithy shape ``com.amazonaws.inspector2#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

IntegrationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "ACTIVE",
    "INACTIVE",
    "DISABLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "ACTIVE",
        "INACTIVE",
        "DISABLING",
    )
)


def serialize_json(value: IntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> IntegrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationStatus value: {data!r}")
    return cast(IntegrationStatus, data)
