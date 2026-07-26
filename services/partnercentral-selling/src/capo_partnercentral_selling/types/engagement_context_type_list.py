"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementContextTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_context_type

EngagementContextTypeList: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementContextTypeList) -> list:
    import capo_partnercentral_selling.types.engagement_context_type

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_context_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementContextTypeList:
    import capo_partnercentral_selling.types.engagement_context_type

    out: EngagementContextTypeList = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.engagement_context_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
