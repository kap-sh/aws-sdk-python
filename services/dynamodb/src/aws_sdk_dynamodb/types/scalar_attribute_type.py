"""Generated from Smithy shape ``com.amazonaws.dynamodb#ScalarAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ScalarAttributeType: TypeAlias = Literal[
    "S",
    "N",
    "B",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S",
        "N",
        "B",
    )
)


def serialize_aws_json_1_0(value: ScalarAttributeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScalarAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalarAttributeType value: {data!r}")
    return cast(ScalarAttributeType, data)
