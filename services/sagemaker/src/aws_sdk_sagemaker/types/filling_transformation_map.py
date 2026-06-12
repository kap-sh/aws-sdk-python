"""Generated from Smithy shape ``com.amazonaws.sagemaker#FillingTransformationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.filling_transformation_value
    import aws_sdk_sagemaker.types.filling_type

FillingTransformationMap: TypeAlias = dict[
    "aws_sdk_sagemaker.types.filling_type.FillingType",
    "aws_sdk_sagemaker.types.filling_transformation_value.FillingTransformationValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FillingTransformationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sagemaker.types.filling_type

        out[aws_sdk_sagemaker.types.filling_type.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> FillingTransformationMap:
    out: FillingTransformationMap = {}
    for key, value in data.items():
        import aws_sdk_sagemaker.types.filling_type

        out[aws_sdk_sagemaker.types.filling_type.deserialize_aws_json_1_1(key)] = value
    return out
