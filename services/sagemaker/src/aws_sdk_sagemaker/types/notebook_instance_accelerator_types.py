"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceAcceleratorTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.notebook_instance_accelerator_type

NotebookInstanceAcceleratorTypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.notebook_instance_accelerator_type.NotebookInstanceAcceleratorType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceAcceleratorTypes) -> list:
    import aws_sdk_sagemaker.types.notebook_instance_accelerator_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.notebook_instance_accelerator_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotebookInstanceAcceleratorTypes:
    import aws_sdk_sagemaker.types.notebook_instance_accelerator_type

    out: NotebookInstanceAcceleratorTypes = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.notebook_instance_accelerator_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
