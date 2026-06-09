"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReturnItemCollectionMetrics``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ReturnItemCollectionMetrics: TypeAlias = Literal[
    "SIZE",
    "NONE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIZE",
        "NONE",
    )
)


def serialize_aws_json_1_0(value: ReturnItemCollectionMetrics) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReturnItemCollectionMetrics:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReturnItemCollectionMetrics value: {data!r}"
        )
    return cast(ReturnItemCollectionMetrics, data)
