"""Generated from Smithy shape ``com.amazonaws.qconnect#AssociationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_association_configuration_type
    import aws_sdk_qconnect.types.association_configuration_data
    import aws_sdk_qconnect.types.uuid


class AssociationConfiguration(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the association for this Association Configuration.</p>"""
    association_type: NotRequired[
        "aws_sdk_qconnect.types.ai_agent_association_configuration_type.AIAgentAssociationConfigurationType"
    ]
    """<p>The type of the association for this Association Configuration.</p>"""
    association_configuration_data: NotRequired[
        "aws_sdk_qconnect.types.association_configuration_data.AssociationConfigurationData"
    ]
    """<p>The data of the configuration for an Amazon Q in Connect Assistant Association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociationConfiguration) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "association_type" in value:
        out["associationType"] = value["association_type"]
    if "association_configuration_data" in value:
        import aws_sdk_qconnect.types.association_configuration_data

        out["associationConfigurationData"] = (
            aws_sdk_qconnect.types.association_configuration_data.serialize_json(
                value["association_configuration_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociationConfiguration:
    out: AssociationConfiguration = {}  # type: ignore[typeddict-item]
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    if "associationType" in data:
        out["association_type"] = data["associationType"]
    if "associationConfigurationData" in data:
        import aws_sdk_qconnect.types.association_configuration_data

        out["association_configuration_data"] = (
            aws_sdk_qconnect.types.association_configuration_data.deserialize_json(
                data["associationConfigurationData"]
            )
        )
    return out
