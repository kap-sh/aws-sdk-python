"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.parameter_value

ParameterValueList: TypeAlias = list[
    "aws_sdk_data_pipeline.types.parameter_value.ParameterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterValueList) -> list:
    import aws_sdk_data_pipeline.types.parameter_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_data_pipeline.types.parameter_value.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterValueList:
    import aws_sdk_data_pipeline.types.parameter_value

    out: ParameterValueList = []
    for item in data:
        out.append(
            aws_sdk_data_pipeline.types.parameter_value.deserialize_aws_json_1_1(item)
        )
    return out
