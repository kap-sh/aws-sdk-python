"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EntityTypeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.entity_metadata
    import aws_sdk_bedrock_data_automation.types.entity_type


class EntityTypeInfo(TypedDict, closed=True):
    entity_type: "aws_sdk_bedrock_data_automation.types.entity_type.EntityType"
    entity_metadata: NotRequired[
        "aws_sdk_bedrock_data_automation.types.entity_metadata.EntityMetadata"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeInfo) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.entity_type

    out["entityType"] = (
        aws_sdk_bedrock_data_automation.types.entity_type.serialize_json(
            value["entity_type"]
        )
    )
    if "entity_metadata" in value:
        out["entityMetadata"] = value["entity_metadata"]
    return out


def deserialize_json(data: dict) -> EntityTypeInfo:
    out: EntityTypeInfo = {}  # type: ignore[typeddict-item]
    if "entityType" in data:
        import aws_sdk_bedrock_data_automation.types.entity_type

        out["entity_type"] = (
            aws_sdk_bedrock_data_automation.types.entity_type.deserialize_json(
                data["entityType"]
            )
        )
    else:
        raise DeserializationError("EntityTypeInfo.entity_type required")
    if "entityMetadata" in data:
        out["entity_metadata"] = data["entityMetadata"]
    return out
