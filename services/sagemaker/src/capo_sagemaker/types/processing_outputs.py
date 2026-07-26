"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_output

ProcessingOutputs: TypeAlias = list[
    "capo_sagemaker.types.processing_output.ProcessingOutput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingOutputs) -> list:
    import capo_sagemaker.types.processing_output

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.processing_output.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProcessingOutputs:
    import capo_sagemaker.types.processing_output

    out: ProcessingOutputs = []
    for item in data:
        out.append(
            capo_sagemaker.types.processing_output.deserialize_aws_json_1_1(item)
        )
    return out
