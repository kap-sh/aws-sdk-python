"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.opportunity_identifier

OpportunityIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> OpportunityIdentifiers:
    return list(data)
