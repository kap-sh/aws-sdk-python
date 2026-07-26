"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateEventConfigurationByResourceTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.connection_status_resource_type_event_configuration
    import capo_iot_wireless.types.device_registration_state_resource_type_event_configuration
    import capo_iot_wireless.types.join_resource_type_event_configuration
    import capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration
    import capo_iot_wireless.types.proximity_resource_type_event_configuration


class UpdateEventConfigurationByResourceTypesRequest(TypedDict, closed=True):
    device_registration_state: NotRequired[
        "capo_iot_wireless.types.device_registration_state_resource_type_event_configuration.DeviceRegistrationStateResourceTypeEventConfiguration"
    ]
    """<p>Device registration state resource type event configuration object for enabling and disabling wireless gateway topic.</p>"""
    proximity: NotRequired[
        "capo_iot_wireless.types.proximity_resource_type_event_configuration.ProximityResourceTypeEventConfiguration"
    ]
    """<p>Proximity resource type event configuration object for enabling and disabling wireless gateway topic.</p>"""
    join: NotRequired[
        "capo_iot_wireless.types.join_resource_type_event_configuration.JoinResourceTypeEventConfiguration"
    ]
    """<p>Join resource type event configuration object for enabling and disabling wireless device topic.</p>"""
    connection_status: NotRequired[
        "capo_iot_wireless.types.connection_status_resource_type_event_configuration.ConnectionStatusResourceTypeEventConfiguration"
    ]
    """<p>Connection status resource type event configuration object for enabling and disabling wireless gateway topic.</p>"""
    message_delivery_status: NotRequired[
        "capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration.MessageDeliveryStatusResourceTypeEventConfiguration"
    ]
    """<p>Message delivery status resource type event configuration object for enabling and disabling wireless device topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventConfigurationByResourceTypesRequest) -> dict:
    out: dict = {}
    if "device_registration_state" in value:
        import capo_iot_wireless.types.device_registration_state_resource_type_event_configuration

        out["DeviceRegistrationState"] = (
            capo_iot_wireless.types.device_registration_state_resource_type_event_configuration.serialize_json(
                value["device_registration_state"]
            )
        )
    if "proximity" in value:
        import capo_iot_wireless.types.proximity_resource_type_event_configuration

        out["Proximity"] = (
            capo_iot_wireless.types.proximity_resource_type_event_configuration.serialize_json(
                value["proximity"]
            )
        )
    if "join" in value:
        import capo_iot_wireless.types.join_resource_type_event_configuration

        out["Join"] = (
            capo_iot_wireless.types.join_resource_type_event_configuration.serialize_json(
                value["join"]
            )
        )
    if "connection_status" in value:
        import capo_iot_wireless.types.connection_status_resource_type_event_configuration

        out["ConnectionStatus"] = (
            capo_iot_wireless.types.connection_status_resource_type_event_configuration.serialize_json(
                value["connection_status"]
            )
        )
    if "message_delivery_status" in value:
        import capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration

        out["MessageDeliveryStatus"] = (
            capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration.serialize_json(
                value["message_delivery_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEventConfigurationByResourceTypesRequest:
    out: UpdateEventConfigurationByResourceTypesRequest = {}  # type: ignore[typeddict-item]
    if "DeviceRegistrationState" in data:
        import capo_iot_wireless.types.device_registration_state_resource_type_event_configuration

        out["device_registration_state"] = (
            capo_iot_wireless.types.device_registration_state_resource_type_event_configuration.deserialize_json(
                data["DeviceRegistrationState"]
            )
        )
    if "Proximity" in data:
        import capo_iot_wireless.types.proximity_resource_type_event_configuration

        out["proximity"] = (
            capo_iot_wireless.types.proximity_resource_type_event_configuration.deserialize_json(
                data["Proximity"]
            )
        )
    if "Join" in data:
        import capo_iot_wireless.types.join_resource_type_event_configuration

        out["join"] = (
            capo_iot_wireless.types.join_resource_type_event_configuration.deserialize_json(
                data["Join"]
            )
        )
    if "ConnectionStatus" in data:
        import capo_iot_wireless.types.connection_status_resource_type_event_configuration

        out["connection_status"] = (
            capo_iot_wireless.types.connection_status_resource_type_event_configuration.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    if "MessageDeliveryStatus" in data:
        import capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration

        out["message_delivery_status"] = (
            capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration.deserialize_json(
                data["MessageDeliveryStatus"]
            )
        )
    return out
