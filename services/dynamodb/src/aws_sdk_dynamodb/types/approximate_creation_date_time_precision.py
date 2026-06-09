"""Generated from Smithy shape ``com.amazonaws.dynamodb#ApproximateCreationDateTimePrecision``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ApproximateCreationDateTimePrecision: TypeAlias = Literal[
    "MILLISECOND",
    "MICROSECOND",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MILLISECOND",
        "MICROSECOND",
    )
)


def serialize_aws_json_1_0(value: ApproximateCreationDateTimePrecision) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ApproximateCreationDateTimePrecision:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ApproximateCreationDateTimePrecision value: {data!r}"
        )
    return cast(ApproximateCreationDateTimePrecision, data)
