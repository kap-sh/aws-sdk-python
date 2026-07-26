"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_arn_or_identifier

EngagementIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> EngagementIdentifiers:
    return list(data)
