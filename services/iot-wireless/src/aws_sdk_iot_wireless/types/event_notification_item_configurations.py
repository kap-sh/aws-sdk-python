"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventNotificationItemConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.connection_status_event_configuration
    import aws_sdk_iot_wireless.types.device_registration_state_event_configuration
    import aws_sdk_iot_wireless.types.join_event_configuration
    import aws_sdk_iot_wireless.types.message_delivery_status_event_configuration
    import aws_sdk_iot_wireless.types.proximity_event_configuration


class EventNotificationItemConfigurations(TypedDict, closed=True):
    device_registration_state: NotRequired[
        "aws_sdk_iot_wireless.types.device_registration_state_event_configuration.DeviceRegistrationStateEventConfiguration"
    ]
    """<p>Device registration state event configuration for an event configuration item.</p>"""
    proximity: NotRequired[
        "aws_sdk_iot_wireless.types.proximity_event_configuration.ProximityEventConfiguration"
    ]
    """<p>Proximity event configuration for an event configuration item.</p>"""
    join: NotRequired[
        "aws_sdk_iot_wireless.types.join_event_configuration.JoinEventConfiguration"
    ]
    """<p>Join event configuration for an event configuration item.</p>"""
    connection_status: NotRequired[
        "aws_sdk_iot_wireless.types.connection_status_event_configuration.ConnectionStatusEventConfiguration"
    ]
    """<p>Connection status event configuration for an event configuration item.</p>"""
    message_delivery_status: NotRequired[
        "aws_sdk_iot_wireless.types.message_delivery_status_event_configuration.MessageDeliveryStatusEventConfiguration"
    ]
    """<p>Message delivery status event configuration for an event configuration item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventNotificationItemConfigurations) -> dict:
    out: dict = {}
    if "device_registration_state" in value:
        import aws_sdk_iot_wireless.types.device_registration_state_event_configuration

        out["DeviceRegistrationState"] = (
            aws_sdk_iot_wireless.types.device_registration_state_event_configuration.serialize_json(
                value["device_registration_state"]
            )
        )
    if "proximity" in value:
        import aws_sdk_iot_wireless.types.proximity_event_configuration

        out["Proximity"] = (
            aws_sdk_iot_wireless.types.proximity_event_configuration.serialize_json(
                value["proximity"]
            )
        )
    if "join" in value:
        import aws_sdk_iot_wireless.types.join_event_configuration

        out["Join"] = (
            aws_sdk_iot_wireless.types.join_event_configuration.serialize_json(
                value["join"]
            )
        )
    if "connection_status" in value:
        import aws_sdk_iot_wireless.types.connection_status_event_configuration

        out["ConnectionStatus"] = (
            aws_sdk_iot_wireless.types.connection_status_event_configuration.serialize_json(
                value["connection_status"]
            )
        )
    if "message_delivery_status" in value:
        import aws_sdk_iot_wireless.types.message_delivery_status_event_configuration

        out["MessageDeliveryStatus"] = (
            aws_sdk_iot_wireless.types.message_delivery_status_event_configuration.serialize_json(
                value["message_delivery_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventNotificationItemConfigurations:
    out: EventNotificationItemConfigurations = {}  # type: ignore[typeddict-item]
    if "DeviceRegistrationState" in data:
        import aws_sdk_iot_wireless.types.device_registration_state_event_configuration

        out["device_registration_state"] = (
            aws_sdk_iot_wireless.types.device_registration_state_event_configuration.deserialize_json(
                data["DeviceRegistrationState"]
            )
        )
    if "Proximity" in data:
        import aws_sdk_iot_wireless.types.proximity_event_configuration

        out["proximity"] = (
            aws_sdk_iot_wireless.types.proximity_event_configuration.deserialize_json(
                data["Proximity"]
            )
        )
    if "Join" in data:
        import aws_sdk_iot_wireless.types.join_event_configuration

        out["join"] = (
            aws_sdk_iot_wireless.types.join_event_configuration.deserialize_json(
                data["Join"]
            )
        )
    if "ConnectionStatus" in data:
        import aws_sdk_iot_wireless.types.connection_status_event_configuration

        out["connection_status"] = (
            aws_sdk_iot_wireless.types.connection_status_event_configuration.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    if "MessageDeliveryStatus" in data:
        import aws_sdk_iot_wireless.types.message_delivery_status_event_configuration

        out["message_delivery_status"] = (
            aws_sdk_iot_wireless.types.message_delivery_status_event_configuration.deserialize_json(
                data["MessageDeliveryStatus"]
            )
        )
    return out
