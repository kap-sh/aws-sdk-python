"""Generated from Smithy shape ``com.amazonaws.ssm#SessionManagerParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.session_manager_parameter_name
    import aws_sdk_ssm.types.session_manager_parameter_value_list

SessionManagerParameters: TypeAlias = dict[
    "aws_sdk_ssm.types.session_manager_parameter_name.SessionManagerParameterName",
    "aws_sdk_ssm.types.session_manager_parameter_value_list.SessionManagerParameterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: SessionManagerParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.session_manager_parameter_value_list

        out[key] = (
            aws_sdk_ssm.types.session_manager_parameter_value_list.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionManagerParameters:
    out: SessionManagerParameters = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.session_manager_parameter_value_list

        out[key] = (
            aws_sdk_ssm.types.session_manager_parameter_value_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out
