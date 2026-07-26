"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementInvitationIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier

EngagementInvitationIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementInvitationIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> EngagementInvitationIdentifiers:
    return list(data)
