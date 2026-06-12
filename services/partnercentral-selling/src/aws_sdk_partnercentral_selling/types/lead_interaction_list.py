"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInteractionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.lead_interaction

LeadInteractionList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.lead_interaction.LeadInteraction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInteractionList) -> list:
    import aws_sdk_partnercentral_selling.types.lead_interaction

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.lead_interaction.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LeadInteractionList:
    import aws_sdk_partnercentral_selling.types.lead_interaction

    out: LeadInteractionList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.lead_interaction.deserialize_aws_json_1_0(
                item
            )
        )
    return out
