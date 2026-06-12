"""Generated from Smithy shape ``com.amazonaws.sagemaker#RealtimeInferenceInstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.production_variant_instance_type

RealtimeInferenceInstanceTypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RealtimeInferenceInstanceTypes) -> list:
    import aws_sdk_sagemaker.types.production_variant_instance_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RealtimeInferenceInstanceTypes:
    import aws_sdk_sagemaker.types.production_variant_instance_type

    out: RealtimeInferenceInstanceTypes = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
