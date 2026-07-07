"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryEntitySummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.vocabulary_entity_summary


class _DataAutomationLibraryEntitySummary_vocabulary(TypedDict, closed=True):
    vocabulary: "aws_sdk_bedrock_data_automation.types.vocabulary_entity_summary.VocabularyEntitySummary"


DataAutomationLibraryEntitySummary: TypeAlias = (
    _DataAutomationLibraryEntitySummary_vocabulary
)


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryEntitySummary) -> dict:
    if "vocabulary" in value:
        import aws_sdk_bedrock_data_automation.types.vocabulary_entity_summary

        return {
            "vocabulary": aws_sdk_bedrock_data_automation.types.vocabulary_entity_summary.serialize_json(
                value["vocabulary"]
            )
        }
    else:
        raise SerializationError(
            "DataAutomationLibraryEntitySummary: no variant present"
        )


def deserialize_json(data: dict) -> DataAutomationLibraryEntitySummary:
    if "vocabulary" in data:
        import aws_sdk_bedrock_data_automation.types.vocabulary_entity_summary

        return {
            "vocabulary": aws_sdk_bedrock_data_automation.types.vocabulary_entity_summary.deserialize_json(
                data["vocabulary"]
            )
        }
    else:
        raise DeserializationError(
            "DataAutomationLibraryEntitySummary: no recognized variant key"
        )
