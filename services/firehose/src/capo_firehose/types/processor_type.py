"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessorType``."""

from typing import Literal, TypeAlias, cast

ProcessorType: TypeAlias = Literal[
    "RecordDeAggregation",
    "Decompression",
    "CloudWatchLogProcessing",
    "Lambda",
    "MetadataExtraction",
    "AppendDelimiterToRecord",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessorType:
    return cast(ProcessorType, data)
