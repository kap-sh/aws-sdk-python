"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_member

EngagementMembers: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_member.EngagementMember"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementMembers) -> list:
    import capo_partnercentral_selling.types.engagement_member

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_member.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementMembers:
    import capo_partnercentral_selling.types.engagement_member

    out: EngagementMembers = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.engagement_member.deserialize_aws_json_1_0(
                item
            )
        )
    return out
