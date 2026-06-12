"""Generated from Smithy shape ``com.amazonaws.configservice#RelationshipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.relationship

RelationshipList: TypeAlias = list[
    "aws_sdk_config_service.types.relationship.Relationship"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationshipList) -> list:
    import aws_sdk_config_service.types.relationship

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.relationship.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationshipList:
    import aws_sdk_config_service.types.relationship

    out: RelationshipList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.relationship.deserialize_aws_json_1_1(item)
        )
    return out
