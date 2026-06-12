"""Generated from Smithy shape ``com.amazonaws.glue#TableAttributes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TableAttributes: TypeAlias = Literal[
    "NAME",
    "TABLE_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "TABLE_TYPE",
    )
)


def serialize_aws_json_1_1(value: TableAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableAttributes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableAttributes value: {data!r}")
    return cast(TableAttributes, data)
