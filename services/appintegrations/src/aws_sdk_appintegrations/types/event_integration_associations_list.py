"""Generated from Smithy shape ``com.amazonaws.appintegrations#EventIntegrationAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.event_integration_association

EventIntegrationAssociationsList: TypeAlias = list["aws_sdk_appintegrations.types.event_integration_association.EventIntegrationAssociation"]


# --- restJson1 ser/de ---
def serialize_json(value: EventIntegrationAssociationsList) -> list:
    import aws_sdk_appintegrations.types.event_integration_association
    out: list = []
    for item in value:
        out.append(aws_sdk_appintegrations.types.event_integration_association.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventIntegrationAssociationsList:
    import aws_sdk_appintegrations.types.event_integration_association
    out: EventIntegrationAssociationsList = []
    for item in data:
        out.append(aws_sdk_appintegrations.types.event_integration_association.deserialize_json(item))
    return out