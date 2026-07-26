"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformInstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.transform_instance_type

TransformInstanceTypes: TypeAlias = list[
    "capo_sagemaker.types.transform_instance_type.TransformInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformInstanceTypes) -> list:
    import capo_sagemaker.types.transform_instance_type

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.transform_instance_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TransformInstanceTypes:
    import capo_sagemaker.types.transform_instance_type

    out: TransformInstanceTypes = []
    for item in data:
        out.append(
            capo_sagemaker.types.transform_instance_type.deserialize_aws_json_1_1(item)
        )
    return out
