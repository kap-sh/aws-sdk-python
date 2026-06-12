"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpsertEntityInfo``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_data_automation.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.vocabulary_entity_info


class _UpsertEntityInfo_vocabulary(TypedDict):
    vocabulary: "aws_sdk_bedrock_data_automation.types.vocabulary_entity_info.VocabularyEntityInfo"


UpsertEntityInfo: TypeAlias = _UpsertEntityInfo_vocabulary


# --- restJson1 ser/de ---
def serialize_json(value: UpsertEntityInfo) -> dict:
    if "vocabulary" in value:
        import aws_sdk_bedrock_data_automation.types.vocabulary_entity_info

        return {
            "vocabulary": aws_sdk_bedrock_data_automation.types.vocabulary_entity_info.serialize_json(
                value["vocabulary"]
            )
        }
    else:
        raise SerializationError("UpsertEntityInfo: no variant present")


def deserialize_json(data: dict) -> UpsertEntityInfo:
    if "vocabulary" in data:
        import aws_sdk_bedrock_data_automation.types.vocabulary_entity_info

        return {
            "vocabulary": aws_sdk_bedrock_data_automation.types.vocabulary_entity_info.deserialize_json(
                data["vocabulary"]
            )
        }
    else:
        raise DeserializationError("UpsertEntityInfo: no recognized variant key")
