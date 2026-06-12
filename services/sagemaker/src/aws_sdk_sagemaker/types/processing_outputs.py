"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_output

ProcessingOutputs: TypeAlias = list[
    "aws_sdk_sagemaker.types.processing_output.ProcessingOutput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingOutputs) -> list:
    import aws_sdk_sagemaker.types.processing_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.processing_output.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProcessingOutputs:
    import aws_sdk_sagemaker.types.processing_output

    out: ProcessingOutputs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.processing_output.deserialize_aws_json_1_1(item)
        )
    return out
