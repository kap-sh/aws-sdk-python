"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

ProcessorType: TypeAlias = Literal[
    "RecordDeAggregation",
    "Decompression",
    "CloudWatchLogProcessing",
    "Lambda",
    "MetadataExtraction",
    "AppendDelimiterToRecord",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RecordDeAggregation",
        "Decompression",
        "CloudWatchLogProcessing",
        "Lambda",
        "MetadataExtraction",
        "AppendDelimiterToRecord",
    )
)


def serialize_aws_json_1_1(value: ProcessorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessorType value: {data!r}")
    return cast(ProcessorType, data)
