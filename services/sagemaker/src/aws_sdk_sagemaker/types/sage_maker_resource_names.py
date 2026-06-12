"""Generated from Smithy shape ``com.amazonaws.sagemaker#SageMakerResourceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.sage_maker_resource_name

SageMakerResourceNames: TypeAlias = list[
    "aws_sdk_sagemaker.types.sage_maker_resource_name.SageMakerResourceName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerResourceNames) -> list:
    import aws_sdk_sagemaker.types.sage_maker_resource_name

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.sage_maker_resource_name.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SageMakerResourceNames:
    import aws_sdk_sagemaker.types.sage_maker_resource_name

    out: SageMakerResourceNames = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.sage_maker_resource_name.deserialize_aws_json_1_1(
                item
            )
        )
    return out
