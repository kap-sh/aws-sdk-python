"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

DeliveryStreamType: TypeAlias = Literal[
    "DirectPut",
    "KinesisStreamAsSource",
    "MSKAsSource",
    "DatabaseAsSource",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DirectPut",
        "KinesisStreamAsSource",
        "MSKAsSource",
        "DatabaseAsSource",
    )
)


def serialize_aws_json_1_1(value: DeliveryStreamType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStreamType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryStreamType value: {data!r}")
    return cast(DeliveryStreamType, data)
