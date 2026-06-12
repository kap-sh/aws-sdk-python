"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

IntentFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CO",
        "EQ",
    )
)


def serialize_json(value: IntentFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> IntentFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntentFilterOperator value: {data!r}")
    return cast(IntentFilterOperator, data)
