"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RecordFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

RecordFormatType: TypeAlias = Literal[
    "JSON",
    "CSV",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "CSV",
    )
)


def serialize_aws_json_1_1(value: RecordFormatType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordFormatType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordFormatType value: {data!r}")
    return cast(RecordFormatType, data)
