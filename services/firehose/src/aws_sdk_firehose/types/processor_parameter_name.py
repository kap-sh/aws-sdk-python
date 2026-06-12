"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessorParameterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

ProcessorParameterName: TypeAlias = Literal[
    "LambdaArn",
    "NumberOfRetries",
    "MetadataExtractionQuery",
    "JsonParsingEngine",
    "RoleArn",
    "BufferSizeInMBs",
    "BufferIntervalInSeconds",
    "SubRecordType",
    "Delimiter",
    "CompressionFormat",
    "DataMessageExtraction",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LambdaArn",
        "NumberOfRetries",
        "MetadataExtractionQuery",
        "JsonParsingEngine",
        "RoleArn",
        "BufferSizeInMBs",
        "BufferIntervalInSeconds",
        "SubRecordType",
        "Delimiter",
        "CompressionFormat",
        "DataMessageExtraction",
    )
)


def serialize_aws_json_1_1(value: ProcessorParameterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessorParameterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessorParameterName value: {data!r}")
    return cast(ProcessorParameterName, data)
