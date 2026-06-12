"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementContexts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_context_details

EngagementContexts: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.engagement_context_details.EngagementContextDetails"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementContexts) -> list:
    import aws_sdk_partnercentral_selling.types.engagement_context_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.engagement_context_details.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementContexts:
    import aws_sdk_partnercentral_selling.types.engagement_context_details

    out: EngagementContexts = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.engagement_context_details.deserialize_aws_json_1_0(
                item
            )
        )
    return out
