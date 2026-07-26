"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementMemberSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_member_summary

EngagementMemberSummaries: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_member_summary.EngagementMemberSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementMemberSummaries) -> list:
    import capo_partnercentral_selling.types.engagement_member_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_member_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementMemberSummaries:
    import capo_partnercentral_selling.types.engagement_member_summary

    out: EngagementMemberSummaries = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.engagement_member_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
