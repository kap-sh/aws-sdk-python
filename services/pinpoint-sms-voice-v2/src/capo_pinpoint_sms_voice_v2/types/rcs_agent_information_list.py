"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsAgentInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_information

RcsAgentInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.rcs_agent_information.RcsAgentInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsAgentInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.rcs_agent_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RcsAgentInformationList:
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_information

    out: RcsAgentInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.rcs_agent_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
