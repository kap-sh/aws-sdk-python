"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementInvitationPayloadType``."""

from typing import Literal, TypeAlias, cast

EngagementInvitationPayloadType: TypeAlias = Literal[
    "OpportunityInvitation",
    "LeadInvitation",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementInvitationPayloadType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementInvitationPayloadType:
    return cast(EngagementInvitationPayloadType, data)
