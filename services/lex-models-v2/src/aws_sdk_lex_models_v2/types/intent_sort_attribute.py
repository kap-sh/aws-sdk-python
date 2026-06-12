"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

IntentSortAttribute: TypeAlias = Literal[
    "IntentName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IntentName",
        "LastUpdatedDateTime",
    )
)


def serialize_json(value: IntentSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> IntentSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntentSortAttribute value: {data!r}")
    return cast(IntentSortAttribute, data)
