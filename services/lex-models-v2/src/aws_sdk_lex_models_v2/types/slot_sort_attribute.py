"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotSortAttribute: TypeAlias = Literal[
    "SlotName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SlotName",
        "LastUpdatedDateTime",
    )
)


def serialize_json(value: SlotSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> SlotSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotSortAttribute value: {data!r}")
    return cast(SlotSortAttribute, data)
