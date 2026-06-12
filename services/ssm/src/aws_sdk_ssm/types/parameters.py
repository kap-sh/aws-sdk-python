"""Generated from Smithy shape ``com.amazonaws.ssm#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_name
    import aws_sdk_ssm.types.parameter_value_list

Parameters: TypeAlias = dict[
    "aws_sdk_ssm.types.parameter_name.ParameterName",
    "aws_sdk_ssm.types.parameter_value_list.ParameterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Parameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.parameter_value_list

        out[key] = aws_sdk_ssm.types.parameter_value_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> Parameters:
    out: Parameters = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.parameter_value_list

        out[key] = aws_sdk_ssm.types.parameter_value_list.deserialize_aws_json_1_1(
            value
        )
    return out
