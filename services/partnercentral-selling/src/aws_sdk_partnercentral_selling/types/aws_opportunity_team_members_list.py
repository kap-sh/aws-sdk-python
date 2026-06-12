"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityTeamMembersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_team_member

AwsOpportunityTeamMembersList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.aws_team_member.AwsTeamMember"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityTeamMembersList) -> list:
    import aws_sdk_partnercentral_selling.types.aws_team_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.aws_team_member.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AwsOpportunityTeamMembersList:
    import aws_sdk_partnercentral_selling.types.aws_team_member

    out: AwsOpportunityTeamMembersList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.aws_team_member.deserialize_aws_json_1_0(
                item
            )
        )
    return out
