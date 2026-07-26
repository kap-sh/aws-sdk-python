"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.parameter_attribute

ParameterAttributeList: TypeAlias = list[
    "capo_data_pipeline.types.parameter_attribute.ParameterAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterAttributeList) -> list:
    import capo_data_pipeline.types.parameter_attribute

    out: list = []
    for item in value:
        out.append(
            capo_data_pipeline.types.parameter_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterAttributeList:
    import capo_data_pipeline.types.parameter_attribute

    out: ParameterAttributeList = []
    for item in data:
        out.append(
            capo_data_pipeline.types.parameter_attribute.deserialize_aws_json_1_1(item)
        )
    return out
