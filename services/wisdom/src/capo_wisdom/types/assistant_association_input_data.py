"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantAssociationInputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_wisdom.types.uuid


class _AssistantAssociationInputData_knowledgeBaseId(TypedDict, closed=True):
    knowledgeBaseId: "capo_wisdom.types.uuid.Uuid"


AssistantAssociationInputData: TypeAlias = (
    _AssistantAssociationInputData_knowledgeBaseId
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationInputData) -> dict:
    if "knowledgeBaseId" in value:
        return {"knowledgeBaseId": value["knowledgeBaseId"]}
    else:
        raise SerializationError("AssistantAssociationInputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationInputData:
    if "knowledgeBaseId" in data:
        return {"knowledgeBaseId": data["knowledgeBaseId"]}
    else:
        raise DeserializationError(
            "AssistantAssociationInputData: no recognized variant key"
        )
