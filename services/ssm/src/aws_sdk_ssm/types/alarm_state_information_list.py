"""Generated from Smithy shape ``com.amazonaws.ssm#AlarmStateInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_state_information

AlarmStateInformationList: TypeAlias = list[
    "aws_sdk_ssm.types.alarm_state_information.AlarmStateInformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmStateInformationList) -> list:
    import aws_sdk_ssm.types.alarm_state_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.alarm_state_information.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AlarmStateInformationList:
    import aws_sdk_ssm.types.alarm_state_information

    out: AlarmStateInformationList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.alarm_state_information.deserialize_aws_json_1_1(item)
        )
    return out
