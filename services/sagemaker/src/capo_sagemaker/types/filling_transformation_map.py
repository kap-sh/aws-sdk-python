"""Generated from Smithy shape ``com.amazonaws.sagemaker#FillingTransformationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.filling_transformation_value
    import capo_sagemaker.types.filling_type

FillingTransformationMap: TypeAlias = dict[
    "capo_sagemaker.types.filling_type.FillingType",
    "capo_sagemaker.types.filling_transformation_value.FillingTransformationValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FillingTransformationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.filling_type

        out[capo_sagemaker.types.filling_type.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> FillingTransformationMap:
    out: FillingTransformationMap = {}
    for key, value in data.items():
        import capo_sagemaker.types.filling_type

        out[capo_sagemaker.types.filling_type.deserialize_aws_json_1_1(key)] = value
    return out
