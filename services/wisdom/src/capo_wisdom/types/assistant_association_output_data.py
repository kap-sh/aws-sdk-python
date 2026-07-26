"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantAssociationOutputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_wisdom.types.knowledge_base_association_data


class _AssistantAssociationOutputData_knowledgeBaseAssociation(TypedDict, closed=True):
    knowledgeBaseAssociation: (
        "capo_wisdom.types.knowledge_base_association_data.KnowledgeBaseAssociationData"
    )


AssistantAssociationOutputData: TypeAlias = (
    _AssistantAssociationOutputData_knowledgeBaseAssociation
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationOutputData) -> dict:
    if "knowledgeBaseAssociation" in value:
        import capo_wisdom.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": capo_wisdom.types.knowledge_base_association_data.serialize_json(
                value["knowledgeBaseAssociation"]
            )
        }
    else:
        raise SerializationError("AssistantAssociationOutputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationOutputData:
    if "knowledgeBaseAssociation" in data:
        import capo_wisdom.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": capo_wisdom.types.knowledge_base_association_data.deserialize_json(
                data["knowledgeBaseAssociation"]
            )
        }
    else:
        raise DeserializationError(
            "AssistantAssociationOutputData: no recognized variant key"
        )
