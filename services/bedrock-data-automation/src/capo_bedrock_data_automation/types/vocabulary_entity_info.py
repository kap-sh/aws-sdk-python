"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VocabularyEntityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.entity_description
    import capo_bedrock_data_automation.types.entity_id
    import capo_bedrock_data_automation.types.language
    import capo_bedrock_data_automation.types.phrase_list


class VocabularyEntityInfo(TypedDict, closed=True):
    entity_id: NotRequired["capo_bedrock_data_automation.types.entity_id.EntityId"]
    description: NotRequired[
        "capo_bedrock_data_automation.types.entity_description.EntityDescription"
    ]
    language: "capo_bedrock_data_automation.types.language.Language"
    phrases: "capo_bedrock_data_automation.types.phrase_list.PhraseList"


# --- restJson1 ser/de ---
def serialize_json(value: VocabularyEntityInfo) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_data_automation.types.language

    out["language"] = capo_bedrock_data_automation.types.language.serialize_json(
        value["language"]
    )
    import capo_bedrock_data_automation.types.phrase_list

    out["phrases"] = capo_bedrock_data_automation.types.phrase_list.serialize_json(
        value["phrases"]
    )
    return out


def deserialize_json(data: dict) -> VocabularyEntityInfo:
    out: VocabularyEntityInfo = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "description" in data:
        out["description"] = data["description"]
    if "language" in data:
        import capo_bedrock_data_automation.types.language

        out["language"] = capo_bedrock_data_automation.types.language.deserialize_json(
            data["language"]
        )
    else:
        raise DeserializationError("VocabularyEntityInfo.language required")
    if "phrases" in data:
        import capo_bedrock_data_automation.types.phrase_list

        out["phrases"] = (
            capo_bedrock_data_automation.types.phrase_list.deserialize_json(
                data["phrases"]
            )
        )
    else:
        raise DeserializationError("VocabularyEntityInfo.phrases required")
    return out
