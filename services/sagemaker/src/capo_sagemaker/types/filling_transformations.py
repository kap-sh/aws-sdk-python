"""Generated from Smithy shape ``com.amazonaws.sagemaker#FillingTransformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.filling_transformation_map
    import capo_sagemaker.types.transformation_attribute_name

FillingTransformations: TypeAlias = dict[
    "capo_sagemaker.types.transformation_attribute_name.TransformationAttributeName",
    "capo_sagemaker.types.filling_transformation_map.FillingTransformationMap",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FillingTransformations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.filling_transformation_map

        out[key] = (
            capo_sagemaker.types.filling_transformation_map.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FillingTransformations:
    out: FillingTransformations = {}
    for key, value in data.items():
        import capo_sagemaker.types.filling_transformation_map

        out[key] = (
            capo_sagemaker.types.filling_transformation_map.deserialize_aws_json_1_1(
                value
            )
        )
    return out
