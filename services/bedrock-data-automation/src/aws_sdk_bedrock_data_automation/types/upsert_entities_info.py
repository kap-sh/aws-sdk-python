"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpsertEntitiesInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.upsert_entity_info

UpsertEntitiesInfo: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.upsert_entity_info.UpsertEntityInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpsertEntitiesInfo) -> list:
    import aws_sdk_bedrock_data_automation.types.upsert_entity_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.upsert_entity_info.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpsertEntitiesInfo:
    import aws_sdk_bedrock_data_automation.types.upsert_entity_info

    out: UpsertEntitiesInfo = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.upsert_entity_info.deserialize_json(
                item
            )
        )
    return out
