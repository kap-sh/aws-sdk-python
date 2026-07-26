"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.assistant_association_id_list


class _KnowledgeSource_assistantAssociationIds(TypedDict, closed=True):
    assistantAssociationIds: (
        "capo_qconnect.types.assistant_association_id_list.AssistantAssociationIdList"
    )


KnowledgeSource: TypeAlias = _KnowledgeSource_assistantAssociationIds


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeSource) -> dict:
    if "assistantAssociationIds" in value:
        import capo_qconnect.types.assistant_association_id_list

        return {
            "assistantAssociationIds": capo_qconnect.types.assistant_association_id_list.serialize_json(
                value["assistantAssociationIds"]
            )
        }
    else:
        raise SerializationError("KnowledgeSource: no variant present")


def deserialize_json(data: dict) -> KnowledgeSource:
    if "assistantAssociationIds" in data:
        import capo_qconnect.types.assistant_association_id_list

        return {
            "assistantAssociationIds": capo_qconnect.types.assistant_association_id_list.deserialize_json(
                data["assistantAssociationIds"]
            )
        }
    else:
        raise DeserializationError("KnowledgeSource: no recognized variant key")
