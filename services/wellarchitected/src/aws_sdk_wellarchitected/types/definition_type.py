"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DefinitionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

DefinitionType: TypeAlias = Literal[
    "WORKLOAD_METADATA",
    "APP_REGISTRY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WORKLOAD_METADATA",
        "APP_REGISTRY",
    )
)


def serialize_json(value: DefinitionType) -> str:
    return value


def deserialize_json(data: str) -> DefinitionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefinitionType value: {data!r}")
    return cast(DefinitionType, data)
