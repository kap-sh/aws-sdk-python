"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessorParameterName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ProcessorParameterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessorParameterName:
    return cast(ProcessorParameterName, data)
