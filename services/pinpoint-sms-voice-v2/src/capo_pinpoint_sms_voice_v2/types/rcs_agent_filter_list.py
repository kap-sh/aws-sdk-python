"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsAgentFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_filter

RcsAgentFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.rcs_agent_filter.RcsAgentFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsAgentFilterList) -> list:
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_filter

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.rcs_agent_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RcsAgentFilterList:
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_filter

    out: RcsAgentFilterList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.rcs_agent_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
