"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RelationshipDisplayNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.relationship_display_name

RelationshipDisplayNameList: TypeAlias = list[
    "aws_sdk_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelationshipDisplayNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RelationshipDisplayNameList:
    return list(data)
