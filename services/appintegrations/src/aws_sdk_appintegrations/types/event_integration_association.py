"""Generated from Smithy shape ``com.amazonaws.appintegrations#EventIntegrationAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.client_association_metadata
    import aws_sdk_appintegrations.types.client_id
    import aws_sdk_appintegrations.types.event_bridge_rule_name
    import aws_sdk_appintegrations.types.name
    import aws_sdk_appintegrations.types.uuid


class EventIntegrationAssociation(TypedDict):
    event_integration_association_arn: NotRequired[
        "aws_sdk_appintegrations.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) for the event integration association.</p>"""
    event_integration_association_id: NotRequired[
        "aws_sdk_appintegrations.types.uuid.UUID"
    ]
    """<p>The identifier for the event integration association.</p>"""
    event_integration_name: NotRequired["aws_sdk_appintegrations.types.name.Name"]
    """<p>The name of the event integration.</p>"""
    client_id: NotRequired["aws_sdk_appintegrations.types.client_id.ClientId"]
    """<p>The identifier for the client that is associated with the event integration.</p>"""
    event_bridge_rule_name: NotRequired[
        "aws_sdk_appintegrations.types.event_bridge_rule_name.EventBridgeRuleName"
    ]
    """<p>The name of the EventBridge rule.</p>"""
    client_association_metadata: NotRequired[
        "aws_sdk_appintegrations.types.client_association_metadata.ClientAssociationMetadata"
    ]
    """<p>The metadata associated with the client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventIntegrationAssociation) -> dict:
    out: dict = {}
    if "event_integration_association_arn" in value:
        out["EventIntegrationAssociationArn"] = value[
            "event_integration_association_arn"
        ]
    if "event_integration_association_id" in value:
        out["EventIntegrationAssociationId"] = value["event_integration_association_id"]
    if "event_integration_name" in value:
        out["EventIntegrationName"] = value["event_integration_name"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "event_bridge_rule_name" in value:
        out["EventBridgeRuleName"] = value["event_bridge_rule_name"]
    if "client_association_metadata" in value:
        import aws_sdk_appintegrations.types.client_association_metadata

        out["ClientAssociationMetadata"] = (
            aws_sdk_appintegrations.types.client_association_metadata.serialize_json(
                value["client_association_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventIntegrationAssociation:
    out: EventIntegrationAssociation = {}  # type: ignore[typeddict-item]
    if "EventIntegrationAssociationArn" in data:
        out["event_integration_association_arn"] = data[
            "EventIntegrationAssociationArn"
        ]
    if "EventIntegrationAssociationId" in data:
        out["event_integration_association_id"] = data["EventIntegrationAssociationId"]
    if "EventIntegrationName" in data:
        out["event_integration_name"] = data["EventIntegrationName"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "EventBridgeRuleName" in data:
        out["event_bridge_rule_name"] = data["EventBridgeRuleName"]
    if "ClientAssociationMetadata" in data:
        import aws_sdk_appintegrations.types.client_association_metadata

        out["client_association_metadata"] = (
            aws_sdk_appintegrations.types.client_association_metadata.deserialize_json(
                data["ClientAssociationMetadata"]
            )
        )
    return out
