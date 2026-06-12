"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementInvitationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_invitation_summary

EngagementInvitationSummaries: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.engagement_invitation_summary.EngagementInvitationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementInvitationSummaries) -> list:
    import aws_sdk_partnercentral_selling.types.engagement_invitation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.engagement_invitation_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementInvitationSummaries:
    import aws_sdk_partnercentral_selling.types.engagement_invitation_summary

    out: EngagementInvitationSummaries = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.engagement_invitation_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
