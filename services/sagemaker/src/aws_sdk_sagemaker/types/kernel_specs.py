"""Generated from Smithy shape ``com.amazonaws.sagemaker#KernelSpecs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.kernel_spec

KernelSpecs: TypeAlias = list["aws_sdk_sagemaker.types.kernel_spec.KernelSpec"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KernelSpecs) -> list:
    import aws_sdk_sagemaker.types.kernel_spec

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.kernel_spec.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KernelSpecs:
    import aws_sdk_sagemaker.types.kernel_spec

    out: KernelSpecs = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.kernel_spec.deserialize_aws_json_1_1(item))
    return out
