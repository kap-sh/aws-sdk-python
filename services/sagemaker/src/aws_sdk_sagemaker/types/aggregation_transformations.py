"""Generated from Smithy shape ``com.amazonaws.sagemaker#AggregationTransformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.aggregation_transformation_value
    import aws_sdk_sagemaker.types.transformation_attribute_name

AggregationTransformations: TypeAlias = dict[
    "aws_sdk_sagemaker.types.transformation_attribute_name.TransformationAttributeName",
    "aws_sdk_sagemaker.types.aggregation_transformation_value.AggregationTransformationValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AggregationTransformations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sagemaker.types.aggregation_transformation_value

        out[key] = (
            aws_sdk_sagemaker.types.aggregation_transformation_value.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregationTransformations:
    out: AggregationTransformations = {}
    for key, value in data.items():
        import aws_sdk_sagemaker.types.aggregation_transformation_value

        out[key] = (
            aws_sdk_sagemaker.types.aggregation_transformation_value.deserialize_aws_json_1_1(
                value
            )
        )
    return out
