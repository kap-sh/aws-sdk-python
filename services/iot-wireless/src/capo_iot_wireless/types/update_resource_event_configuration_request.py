"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateResourceEventConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.connection_status_event_configuration
    import capo_iot_wireless.types.device_registration_state_event_configuration
    import capo_iot_wireless.types.event_notification_partner_type
    import capo_iot_wireless.types.identifier
    import capo_iot_wireless.types.identifier_type
    import capo_iot_wireless.types.join_event_configuration
    import capo_iot_wireless.types.message_delivery_status_event_configuration
    import capo_iot_wireless.types.proximity_event_configuration


class UpdateResourceEventConfigurationRequest(TypedDict, closed=True):
    identifier: "capo_iot_wireless.types.identifier.Identifier"
    """<p>Resource identifier to opt in for event messaging.</p>"""
    identifier_type: "capo_iot_wireless.types.identifier_type.IdentifierType"
    """<p>Identifier type of the particular resource identifier for event configuration.</p>"""
    partner_type: NotRequired[
        "capo_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
    ]
    """<p>Partner type of the resource if the identifier type is <code>PartnerAccountId</code> </p>"""
    device_registration_state: NotRequired[
        "capo_iot_wireless.types.device_registration_state_event_configuration.DeviceRegistrationStateEventConfiguration"
    ]
    """<p>Event configuration for the device registration state event.</p>"""
    proximity: NotRequired[
        "capo_iot_wireless.types.proximity_event_configuration.ProximityEventConfiguration"
    ]
    """<p>Event configuration for the proximity event.</p>"""
    join: NotRequired[
        "capo_iot_wireless.types.join_event_configuration.JoinEventConfiguration"
    ]
    """<p>Event configuration for the join event.</p>"""
    connection_status: NotRequired[
        "capo_iot_wireless.types.connection_status_event_configuration.ConnectionStatusEventConfiguration"
    ]
    """<p>Event configuration for the connection status event.</p>"""
    message_delivery_status: NotRequired[
        "capo_iot_wireless.types.message_delivery_status_event_configuration.MessageDeliveryStatusEventConfiguration"
    ]
    """<p>Event configuration for the message delivery status event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceEventConfigurationRequest) -> dict:
    out: dict = {}
    if "device_registration_state" in value:
        import capo_iot_wireless.types.device_registration_state_event_configuration

        out["DeviceRegistrationState"] = (
            capo_iot_wireless.types.device_registration_state_event_configuration.serialize_json(
                value["device_registration_state"]
            )
        )
    if "proximity" in value:
        import capo_iot_wireless.types.proximity_event_configuration

        out["Proximity"] = (
            capo_iot_wireless.types.proximity_event_configuration.serialize_json(
                value["proximity"]
            )
        )
    if "join" in value:
        import capo_iot_wireless.types.join_event_configuration

        out["Join"] = capo_iot_wireless.types.join_event_configuration.serialize_json(
            value["join"]
        )
    if "connection_status" in value:
        import capo_iot_wireless.types.connection_status_event_configuration

        out["ConnectionStatus"] = (
            capo_iot_wireless.types.connection_status_event_configuration.serialize_json(
                value["connection_status"]
            )
        )
    if "message_delivery_status" in value:
        import capo_iot_wireless.types.message_delivery_status_event_configuration

        out["MessageDeliveryStatus"] = (
            capo_iot_wireless.types.message_delivery_status_event_configuration.serialize_json(
                value["message_delivery_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResourceEventConfigurationRequest:
    out: UpdateResourceEventConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "DeviceRegistrationState" in data:
        import capo_iot_wireless.types.device_registration_state_event_configuration

        out["device_registration_state"] = (
            capo_iot_wireless.types.device_registration_state_event_configuration.deserialize_json(
                data["DeviceRegistrationState"]
            )
        )
    if "Proximity" in data:
        import capo_iot_wireless.types.proximity_event_configuration

        out["proximity"] = (
            capo_iot_wireless.types.proximity_event_configuration.deserialize_json(
                data["Proximity"]
            )
        )
    if "Join" in data:
        import capo_iot_wireless.types.join_event_configuration

        out["join"] = capo_iot_wireless.types.join_event_configuration.deserialize_json(
            data["Join"]
        )
    if "ConnectionStatus" in data:
        import capo_iot_wireless.types.connection_status_event_configuration

        out["connection_status"] = (
            capo_iot_wireless.types.connection_status_event_configuration.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    if "MessageDeliveryStatus" in data:
        import capo_iot_wireless.types.message_delivery_status_event_configuration

        out["message_delivery_status"] = (
            capo_iot_wireless.types.message_delivery_status_event_configuration.deserialize_json(
                data["MessageDeliveryStatus"]
            )
        )
    return out
