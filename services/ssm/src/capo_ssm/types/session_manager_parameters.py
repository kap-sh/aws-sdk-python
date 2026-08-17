"""Generated from Smithy shape ``com.amazonaws.ssm#SessionManagerParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.session_manager_parameter_name
    import capo_ssm.types.session_manager_parameter_value_list

SessionManagerParameters: TypeAlias = dict[
    "capo_ssm.types.session_manager_parameter_name.SessionManagerParameterName",
    "capo_ssm.types.session_manager_parameter_value_list.SessionManagerParameterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: SessionManagerParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm.types.session_manager_parameter_value_list

        out[key] = (
            capo_ssm.types.session_manager_parameter_value_list.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionManagerParameters:
    out: SessionManagerParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_ssm.types.session_manager_parameter_value_list

        out[key] = (
            capo_ssm.types.session_manager_parameter_value_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out
