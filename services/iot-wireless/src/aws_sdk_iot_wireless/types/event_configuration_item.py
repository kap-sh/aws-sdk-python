"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventConfigurationItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.event_notification_item_configurations
    import aws_sdk_iot_wireless.types.event_notification_partner_type
    import aws_sdk_iot_wireless.types.identifier
    import aws_sdk_iot_wireless.types.identifier_type


class EventConfigurationItem(TypedDict):
    identifier: NotRequired["aws_sdk_iot_wireless.types.identifier.Identifier"]
    """<p>Resource identifier opted in for event messaging.</p>"""
    identifier_type: NotRequired[
        "aws_sdk_iot_wireless.types.identifier_type.IdentifierType"
    ]
    """<p>Identifier type of the particular resource identifier for event configuration.</p>"""
    partner_type: NotRequired[
        "aws_sdk_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
    ]
    """<p>Partner type of the resource if the identifier type is PartnerAccountId.</p>"""
    events: NotRequired[
        "aws_sdk_iot_wireless.types.event_notification_item_configurations.EventNotificationItemConfigurations"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EventConfigurationItem) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "identifier_type" in value:
        import aws_sdk_iot_wireless.types.identifier_type

        out["IdentifierType"] = (
            aws_sdk_iot_wireless.types.identifier_type.serialize_json(
                value["identifier_type"]
            )
        )
    if "partner_type" in value:
        import aws_sdk_iot_wireless.types.event_notification_partner_type

        out["PartnerType"] = (
            aws_sdk_iot_wireless.types.event_notification_partner_type.serialize_json(
                value["partner_type"]
            )
        )
    if "events" in value:
        import aws_sdk_iot_wireless.types.event_notification_item_configurations

        out["Events"] = (
            aws_sdk_iot_wireless.types.event_notification_item_configurations.serialize_json(
                value["events"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventConfigurationItem:
    out: EventConfigurationItem = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "IdentifierType" in data:
        import aws_sdk_iot_wireless.types.identifier_type

        out["identifier_type"] = (
            aws_sdk_iot_wireless.types.identifier_type.deserialize_json(
                data["IdentifierType"]
            )
        )
    if "PartnerType" in data:
        import aws_sdk_iot_wireless.types.event_notification_partner_type

        out["partner_type"] = (
            aws_sdk_iot_wireless.types.event_notification_partner_type.deserialize_json(
                data["PartnerType"]
            )
        )
    if "Events" in data:
        import aws_sdk_iot_wireless.types.event_notification_item_configurations

        out["events"] = (
            aws_sdk_iot_wireless.types.event_notification_item_configurations.deserialize_json(
                data["Events"]
            )
        )
    return out
