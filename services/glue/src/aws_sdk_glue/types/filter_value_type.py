"""Generated from Smithy shape ``com.amazonaws.glue#FilterValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FilterValueType: TypeAlias = Literal[
    "COLUMNEXTRACTED",
    "CONSTANT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLUMNEXTRACTED",
        "CONSTANT",
    )
)


def serialize_aws_json_1_1(value: FilterValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterValueType value: {data!r}")
    return cast(FilterValueType, data)
