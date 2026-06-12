"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.parameter_object

ParameterObjectList: TypeAlias = list[
    "aws_sdk_data_pipeline.types.parameter_object.ParameterObject"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterObjectList) -> list:
    import aws_sdk_data_pipeline.types.parameter_object

    out: list = []
    for item in value:
        out.append(
            aws_sdk_data_pipeline.types.parameter_object.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterObjectList:
    import aws_sdk_data_pipeline.types.parameter_object

    out: ParameterObjectList = []
    for item in data:
        out.append(
            aws_sdk_data_pipeline.types.parameter_object.deserialize_aws_json_1_1(item)
        )
    return out
