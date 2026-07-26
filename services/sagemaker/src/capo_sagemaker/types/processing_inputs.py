"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_input

ProcessingInputs: TypeAlias = list[
    "capo_sagemaker.types.processing_input.ProcessingInput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingInputs) -> list:
    import capo_sagemaker.types.processing_input

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.processing_input.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProcessingInputs:
    import capo_sagemaker.types.processing_input

    out: ProcessingInputs = []
    for item in data:
        out.append(capo_sagemaker.types.processing_input.deserialize_aws_json_1_1(item))
    return out
