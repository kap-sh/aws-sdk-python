"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.automation_parameter_key
    import capo_ssm.types.automation_parameter_value_list

AutomationParameterMap: TypeAlias = dict[
    "capo_ssm.types.automation_parameter_key.AutomationParameterKey",
    "capo_ssm.types.automation_parameter_value_list.AutomationParameterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AutomationParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm.types.automation_parameter_value_list

        out[key] = (
            capo_ssm.types.automation_parameter_value_list.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationParameterMap:
    out: AutomationParameterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_ssm.types.automation_parameter_value_list

        out[key] = (
            capo_ssm.types.automation_parameter_value_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out
