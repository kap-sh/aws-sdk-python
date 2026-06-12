"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RelationshipSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.relationship_summary

RelationshipSummaries: TypeAlias = list[
    "aws_sdk_partnercentral_channel.types.relationship_summary.RelationshipSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelationshipSummaries) -> list:
    import aws_sdk_partnercentral_channel.types.relationship_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_channel.types.relationship_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RelationshipSummaries:
    import aws_sdk_partnercentral_channel.types.relationship_summary

    out: RelationshipSummaries = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_channel.types.relationship_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
