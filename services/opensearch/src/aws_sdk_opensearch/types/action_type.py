"""Generated from Smithy shape ``com.amazonaws.opensearch#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "SERVICE_SOFTWARE_UPDATE",
    "JVM_HEAP_SIZE_TUNING",
    "JVM_YOUNG_GEN_TUNING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_SOFTWARE_UPDATE",
        "JVM_HEAP_SIZE_TUNING",
        "JVM_YOUNG_GEN_TUNING",
    )
)


def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
