"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ParameterType``."""

from typing import Literal, TypeAlias, cast

ParameterType: TypeAlias = Literal[
    "SMALLINT",
    "INTEGER",
    "BIGINT",
    "DECIMAL",
    "REAL",
    "DOUBLE_PRECISION",
    "BOOLEAN",
    "CHAR",
    "VARCHAR",
    "DATE",
    "TIMESTAMP",
    "TIMESTAMPTZ",
    "TIME",
    "TIMETZ",
    "VARBYTE",
    "BINARY",
    "BYTE",
    "CHARACTER",
    "DOUBLE",
    "FLOAT",
    "INT",
    "LONG",
    "NUMERIC",
    "SHORT",
    "STRING",
    "TIMESTAMP_LTZ",
    "TIMESTAMP_NTZ",
    "TINYINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterType) -> str:
    return value


def deserialize_json(data: str) -> ParameterType:
    return cast(ParameterType, data)
