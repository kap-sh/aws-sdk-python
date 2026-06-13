"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeSource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_association_id_list


class _KnowledgeSource_assistantAssociationIds(TypedDict):
    assistantAssociationIds: "aws_sdk_qconnect.types.assistant_association_id_list.AssistantAssociationIdList"


KnowledgeSource: TypeAlias = _KnowledgeSource_assistantAssociationIds


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeSource) -> dict:
    if "assistantAssociationIds" in value:
        import aws_sdk_qconnect.types.assistant_association_id_list

        return {
            "assistantAssociationIds": aws_sdk_qconnect.types.assistant_association_id_list.serialize_json(
                value["assistantAssociationIds"]
            )
        }
    else:
        raise SerializationError("KnowledgeSource: no variant present")


def deserialize_json(data: dict) -> KnowledgeSource:
    if "assistantAssociationIds" in data:
        import aws_sdk_qconnect.types.assistant_association_id_list

        return {
            "assistantAssociationIds": aws_sdk_qconnect.types.assistant_association_id_list.deserialize_json(
                data["assistantAssociationIds"]
            )
        }
    else:
        raise DeserializationError("KnowledgeSource: no recognized variant key")
