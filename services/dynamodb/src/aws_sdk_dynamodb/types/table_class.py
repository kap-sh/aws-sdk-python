"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

TableClass: TypeAlias = Literal[
    "STANDARD",
    "STANDARD_INFREQUENT_ACCESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "STANDARD_INFREQUENT_ACCESS",
    )
)


def serialize_aws_json_1_0(value: TableClass) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TableClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableClass value: {data!r}")
    return cast(TableClass, data)
