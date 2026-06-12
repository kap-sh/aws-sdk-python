"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_parameter_key
    import aws_sdk_ssm.types.automation_parameter_value_list

AutomationParameterMap: TypeAlias = dict[
    "aws_sdk_ssm.types.automation_parameter_key.AutomationParameterKey",
    "aws_sdk_ssm.types.automation_parameter_value_list.AutomationParameterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AutomationParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.automation_parameter_value_list

        out[key] = (
            aws_sdk_ssm.types.automation_parameter_value_list.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationParameterMap:
    out: AutomationParameterMap = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.automation_parameter_value_list

        out[key] = (
            aws_sdk_ssm.types.automation_parameter_value_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out
