"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.parameter_object

ParameterObjectList: TypeAlias = list[
    "capo_data_pipeline.types.parameter_object.ParameterObject"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterObjectList) -> list:
    import capo_data_pipeline.types.parameter_object

    out: list = []
    for item in value:
        out.append(
            capo_data_pipeline.types.parameter_object.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterObjectList:
    import capo_data_pipeline.types.parameter_object

    out: ParameterObjectList = []
    for item in data:
        out.append(
            capo_data_pipeline.types.parameter_object.deserialize_aws_json_1_1(item)
        )
    return out
