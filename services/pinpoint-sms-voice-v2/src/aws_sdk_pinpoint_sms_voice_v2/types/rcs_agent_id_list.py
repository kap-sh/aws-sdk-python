"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsAgentIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn

RcsAgentIdList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsAgentIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RcsAgentIdList:
    return list(data)
