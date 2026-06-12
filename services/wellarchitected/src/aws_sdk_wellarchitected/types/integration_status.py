"""Generated from Smithy shape ``com.amazonaws.wellarchitected#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

IntegrationStatus: TypeAlias = Literal[
    "CONFIGURED",
    "NOT_CONFIGURED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFIGURED",
        "NOT_CONFIGURED",
    )
)


def serialize_json(value: IntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> IntegrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationStatus value: {data!r}")
    return cast(IntegrationStatus, data)
