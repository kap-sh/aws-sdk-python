"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessorParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.processor_parameter

ProcessorParameterList: TypeAlias = list[
    "aws_sdk_firehose.types.processor_parameter.ProcessorParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessorParameterList) -> list:
    import aws_sdk_firehose.types.processor_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_firehose.types.processor_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProcessorParameterList:
    import aws_sdk_firehose.types.processor_parameter

    out: ProcessorParameterList = []
    for item in data:
        out.append(
            aws_sdk_firehose.types.processor_parameter.deserialize_aws_json_1_1(item)
        )
    return out
