"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VocabularyEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.date_timestamp
    import aws_sdk_bedrock_data_automation.types.entity_description
    import aws_sdk_bedrock_data_automation.types.entity_id
    import aws_sdk_bedrock_data_automation.types.language
    import aws_sdk_bedrock_data_automation.types.phrase_list


class VocabularyEntity(TypedDict, closed=True):
    entity_id: NotRequired["aws_sdk_bedrock_data_automation.types.entity_id.EntityId"]
    description: NotRequired[
        "aws_sdk_bedrock_data_automation.types.entity_description.EntityDescription"
    ]
    language: NotRequired["aws_sdk_bedrock_data_automation.types.language.Language"]
    phrases: NotRequired["aws_sdk_bedrock_data_automation.types.phrase_list.PhraseList"]
    last_modified_time: NotRequired[
        "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VocabularyEntity) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "language" in value:
        import aws_sdk_bedrock_data_automation.types.language

        out["language"] = aws_sdk_bedrock_data_automation.types.language.serialize_json(
            value["language"]
        )
    if "phrases" in value:
        import aws_sdk_bedrock_data_automation.types.phrase_list

        out["phrases"] = (
            aws_sdk_bedrock_data_automation.types.phrase_list.serialize_json(
                value["phrases"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["lastModifiedTime"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> VocabularyEntity:
    out: VocabularyEntity = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "description" in data:
        out["description"] = data["description"]
    if "language" in data:
        import aws_sdk_bedrock_data_automation.types.language

        out["language"] = (
            aws_sdk_bedrock_data_automation.types.language.deserialize_json(
                data["language"]
            )
        )
    if "phrases" in data:
        import aws_sdk_bedrock_data_automation.types.phrase_list

        out["phrases"] = (
            aws_sdk_bedrock_data_automation.types.phrase_list.deserialize_json(
                data["phrases"]
            )
        )
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    return out
