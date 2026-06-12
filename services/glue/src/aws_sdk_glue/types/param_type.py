"""Generated from Smithy shape ``com.amazonaws.glue#ParamType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ParamType: TypeAlias = Literal[
    "str",
    "int",
    "float",
    "complex",
    "bool",
    "list",
    "null",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "str",
        "int",
        "float",
        "complex",
        "bool",
        "list",
        "null",
    )
)


def serialize_aws_json_1_1(value: ParamType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParamType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParamType value: {data!r}")
    return cast(ParamType, data)
