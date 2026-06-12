"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotTypeSortAttribute: TypeAlias = Literal[
    "SlotTypeName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SlotTypeName",
        "LastUpdatedDateTime",
    )
)


def serialize_json(value: SlotTypeSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotTypeSortAttribute value: {data!r}")
    return cast(SlotTypeSortAttribute, data)
