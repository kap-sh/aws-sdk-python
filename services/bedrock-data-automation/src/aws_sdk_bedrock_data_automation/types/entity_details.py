"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EntityDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.vocabulary_entity


class _EntityDetails_vocabulary(TypedDict, closed=True):
    vocabulary: (
        "aws_sdk_bedrock_data_automation.types.vocabulary_entity.VocabularyEntity"
    )


EntityDetails: TypeAlias = _EntityDetails_vocabulary


# --- restJson1 ser/de ---
def serialize_json(value: EntityDetails) -> dict:
    if "vocabulary" in value:
        import aws_sdk_bedrock_data_automation.types.vocabulary_entity

        return {
            "vocabulary": aws_sdk_bedrock_data_automation.types.vocabulary_entity.serialize_json(
                value["vocabulary"]
            )
        }
    else:
        raise SerializationError("EntityDetails: no variant present")


def deserialize_json(data: dict) -> EntityDetails:
    if "vocabulary" in data:
        import aws_sdk_bedrock_data_automation.types.vocabulary_entity

        return {
            "vocabulary": aws_sdk_bedrock_data_automation.types.vocabulary_entity.deserialize_json(
                data["vocabulary"]
            )
        }
    else:
        raise DeserializationError("EntityDetails: no recognized variant key")
