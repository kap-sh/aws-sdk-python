"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#PartnerOpportunityTeamMembersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.contact

PartnerOpportunityTeamMembersList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.contact.Contact"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerOpportunityTeamMembersList) -> list:
    import aws_sdk_partnercentral_selling.types.contact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.contact.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PartnerOpportunityTeamMembersList:
    import aws_sdk_partnercentral_selling.types.contact

    out: PartnerOpportunityTeamMembersList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.contact.deserialize_aws_json_1_0(item)
        )
    return out
