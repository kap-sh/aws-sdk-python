"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InlinePayload``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_data_automation.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.delete_entities_info
    import aws_sdk_bedrock_data_automation.types.upsert_entities_info


class _InlinePayload_upsertEntitiesInfo(TypedDict):
    upsertEntitiesInfo: (
        "aws_sdk_bedrock_data_automation.types.upsert_entities_info.UpsertEntitiesInfo"
    )


class _InlinePayload_deleteEntitiesInfo(TypedDict):
    deleteEntitiesInfo: (
        "aws_sdk_bedrock_data_automation.types.delete_entities_info.DeleteEntitiesInfo"
    )


InlinePayload: TypeAlias = (
    _InlinePayload_upsertEntitiesInfo | _InlinePayload_deleteEntitiesInfo
)


# --- restJson1 ser/de ---
def serialize_json(value: InlinePayload) -> dict:
    if "upsertEntitiesInfo" in value:
        import aws_sdk_bedrock_data_automation.types.upsert_entities_info

        return {
            "upsertEntitiesInfo": aws_sdk_bedrock_data_automation.types.upsert_entities_info.serialize_json(
                value["upsertEntitiesInfo"]
            )
        }
    elif "deleteEntitiesInfo" in value:
        import aws_sdk_bedrock_data_automation.types.delete_entities_info

        return {
            "deleteEntitiesInfo": aws_sdk_bedrock_data_automation.types.delete_entities_info.serialize_json(
                value["deleteEntitiesInfo"]
            )
        }
    else:
        raise SerializationError("InlinePayload: no variant present")


def deserialize_json(data: dict) -> InlinePayload:
    if "upsertEntitiesInfo" in data:
        import aws_sdk_bedrock_data_automation.types.upsert_entities_info

        return {
            "upsertEntitiesInfo": aws_sdk_bedrock_data_automation.types.upsert_entities_info.deserialize_json(
                data["upsertEntitiesInfo"]
            )
        }
    elif "deleteEntitiesInfo" in data:
        import aws_sdk_bedrock_data_automation.types.delete_entities_info

        return {
            "deleteEntitiesInfo": aws_sdk_bedrock_data_automation.types.delete_entities_info.deserialize_json(
                data["deleteEntitiesInfo"]
            )
        }
    else:
        raise DeserializationError("InlinePayload: no recognized variant key")
