"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DiscoveryIntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

DiscoveryIntegrationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DiscoveryIntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryIntegrationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DiscoveryIntegrationStatus value: {data!r}"
        )
    return cast(DiscoveryIntegrationStatus, data)
