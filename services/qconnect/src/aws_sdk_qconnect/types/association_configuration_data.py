"""Generated from Smithy shape ``com.amazonaws.qconnect#AssociationConfigurationData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.knowledge_base_association_configuration_data


class _AssociationConfigurationData_knowledgeBaseAssociationConfigurationData(
    TypedDict, closed=True
):
    knowledgeBaseAssociationConfigurationData: "aws_sdk_qconnect.types.knowledge_base_association_configuration_data.KnowledgeBaseAssociationConfigurationData"


AssociationConfigurationData: TypeAlias = (
    _AssociationConfigurationData_knowledgeBaseAssociationConfigurationData
)


# --- restJson1 ser/de ---
def serialize_json(value: AssociationConfigurationData) -> dict:
    if "knowledgeBaseAssociationConfigurationData" in value:
        import aws_sdk_qconnect.types.knowledge_base_association_configuration_data

        return {
            "knowledgeBaseAssociationConfigurationData": aws_sdk_qconnect.types.knowledge_base_association_configuration_data.serialize_json(
                value["knowledgeBaseAssociationConfigurationData"]
            )
        }
    else:
        raise SerializationError("AssociationConfigurationData: no variant present")


def deserialize_json(data: dict) -> AssociationConfigurationData:
    if "knowledgeBaseAssociationConfigurationData" in data:
        import aws_sdk_qconnect.types.knowledge_base_association_configuration_data

        return {
            "knowledgeBaseAssociationConfigurationData": aws_sdk_qconnect.types.knowledge_base_association_configuration_data.deserialize_json(
                data["knowledgeBaseAssociationConfigurationData"]
            )
        }
    else:
        raise DeserializationError(
            "AssociationConfigurationData: no recognized variant key"
        )
