"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

ManagedThingAssociationStatus: TypeAlias = Literal[
    "PRE_ASSOCIATED",
    "ASSOCIATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_ASSOCIATED",
        "ASSOCIATED",
    )
)


def serialize_json(value: ManagedThingAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> ManagedThingAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ManagedThingAssociationStatus value: {data!r}"
        )
    return cast(ManagedThingAssociationStatus, data)
