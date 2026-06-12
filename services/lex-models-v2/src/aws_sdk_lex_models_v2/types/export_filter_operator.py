"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ExportFilterOperator: TypeAlias = Literal[
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


def serialize_json(value: ExportFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> ExportFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportFilterOperator value: {data!r}")
    return cast(ExportFilterOperator, data)
