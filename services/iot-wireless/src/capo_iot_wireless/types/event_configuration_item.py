"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventConfigurationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_notification_item_configurations
    import capo_iot_wireless.types.event_notification_partner_type
    import capo_iot_wireless.types.identifier
    import capo_iot_wireless.types.identifier_type


class EventConfigurationItem(TypedDict, closed=True):
    identifier: NotRequired["capo_iot_wireless.types.identifier.Identifier"]
    """<p>Resource identifier opted in for event messaging.</p>"""
    identifier_type: NotRequired[
        "capo_iot_wireless.types.identifier_type.IdentifierType"
    ]
    """<p>Identifier type of the particular resource identifier for event configuration.</p>"""
    partner_type: NotRequired[
        "capo_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
    ]
    """<p>Partner type of the resource if the identifier type is PartnerAccountId.</p>"""
    events: NotRequired[
        "capo_iot_wireless.types.event_notification_item_configurations.EventNotificationItemConfigurations"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EventConfigurationItem) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "identifier_type" in value:
        import capo_iot_wireless.types.identifier_type

        out["IdentifierType"] = capo_iot_wireless.types.identifier_type.serialize_json(
            value["identifier_type"]
        )
    if "partner_type" in value:
        import capo_iot_wireless.types.event_notification_partner_type

        out["PartnerType"] = (
            capo_iot_wireless.types.event_notification_partner_type.serialize_json(
                value["partner_type"]
            )
        )
    if "events" in value:
        import capo_iot_wireless.types.event_notification_item_configurations

        out["Events"] = (
            capo_iot_wireless.types.event_notification_item_configurations.serialize_json(
                value["events"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventConfigurationItem:
    out: EventConfigurationItem = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "IdentifierType" in data:
        import capo_iot_wireless.types.identifier_type

        out["identifier_type"] = (
            capo_iot_wireless.types.identifier_type.deserialize_json(
                data["IdentifierType"]
            )
        )
    if "PartnerType" in data:
        import capo_iot_wireless.types.event_notification_partner_type

        out["partner_type"] = (
            capo_iot_wireless.types.event_notification_partner_type.deserialize_json(
                data["PartnerType"]
            )
        )
    if "Events" in data:
        import capo_iot_wireless.types.event_notification_item_configurations

        out["events"] = (
            capo_iot_wireless.types.event_notification_item_configurations.deserialize_json(
                data["Events"]
            )
        )
    return out
