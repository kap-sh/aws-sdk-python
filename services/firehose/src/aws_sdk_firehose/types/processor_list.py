"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.processor

ProcessorList: TypeAlias = list["aws_sdk_firehose.types.processor.Processor"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessorList) -> list:
    import aws_sdk_firehose.types.processor

    out: list = []
    for item in value:
        out.append(aws_sdk_firehose.types.processor.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProcessorList:
    import aws_sdk_firehose.types.processor

    out: ProcessorList = []
    for item in data:
        out.append(aws_sdk_firehose.types.processor.deserialize_aws_json_1_1(item))
    return out
