"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementInvitationsPayloadType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_invitation_payload_type

EngagementInvitationsPayloadType: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_invitation_payload_type.EngagementInvitationPayloadType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementInvitationsPayloadType) -> list:
    import capo_partnercentral_selling.types.engagement_invitation_payload_type

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_invitation_payload_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementInvitationsPayloadType:
    import capo_partnercentral_selling.types.engagement_invitation_payload_type

    out: EngagementInvitationsPayloadType = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.engagement_invitation_payload_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
