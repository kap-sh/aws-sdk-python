"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ImportFilterOperator: TypeAlias = Literal[
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


def serialize_json(value: ImportFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> ImportFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportFilterOperator value: {data!r}")
    return cast(ImportFilterOperator, data)
