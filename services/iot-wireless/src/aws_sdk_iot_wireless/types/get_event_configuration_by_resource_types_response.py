"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetEventConfigurationByResourceTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.join_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration


class GetEventConfigurationByResourceTypesResponse(TypedDict, closed=True):
    device_registration_state: NotRequired[
        "aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration.DeviceRegistrationStateResourceTypeEventConfiguration"
    ]
    """<p>Resource type event configuration for the device registration state event.</p>"""
    proximity: NotRequired[
        "aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration.ProximityResourceTypeEventConfiguration"
    ]
    """<p>Resource type event configuration for the proximity event.</p>"""
    join: NotRequired[
        "aws_sdk_iot_wireless.types.join_resource_type_event_configuration.JoinResourceTypeEventConfiguration"
    ]
    """<p>Resource type event configuration for the join event.</p>"""
    connection_status: NotRequired[
        "aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration.ConnectionStatusResourceTypeEventConfiguration"
    ]
    """<p>Resource type event configuration for the connection status event.</p>"""
    message_delivery_status: NotRequired[
        "aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration.MessageDeliveryStatusResourceTypeEventConfiguration"
    ]
    """<p>Resource type event configuration object for the message delivery status event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventConfigurationByResourceTypesResponse) -> dict:
    out: dict = {}
    if "device_registration_state" in value:
        import aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration

        out["DeviceRegistrationState"] = (
            aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration.serialize_json(
                value["device_registration_state"]
            )
        )
    if "proximity" in value:
        import aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration

        out["Proximity"] = (
            aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration.serialize_json(
                value["proximity"]
            )
        )
    if "join" in value:
        import aws_sdk_iot_wireless.types.join_resource_type_event_configuration

        out["Join"] = (
            aws_sdk_iot_wireless.types.join_resource_type_event_configuration.serialize_json(
                value["join"]
            )
        )
    if "connection_status" in value:
        import aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration

        out["ConnectionStatus"] = (
            aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration.serialize_json(
                value["connection_status"]
            )
        )
    if "message_delivery_status" in value:
        import aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration

        out["MessageDeliveryStatus"] = (
            aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration.serialize_json(
                value["message_delivery_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEventConfigurationByResourceTypesResponse:
    out: GetEventConfigurationByResourceTypesResponse = {}  # type: ignore[typeddict-item]
    if "DeviceRegistrationState" in data:
        import aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration

        out["device_registration_state"] = (
            aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration.deserialize_json(
                data["DeviceRegistrationState"]
            )
        )
    if "Proximity" in data:
        import aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration

        out["proximity"] = (
            aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration.deserialize_json(
                data["Proximity"]
            )
        )
    if "Join" in data:
        import aws_sdk_iot_wireless.types.join_resource_type_event_configuration

        out["join"] = (
            aws_sdk_iot_wireless.types.join_resource_type_event_configuration.deserialize_json(
                data["Join"]
            )
        )
    if "ConnectionStatus" in data:
        import aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration

        out["connection_status"] = (
            aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    if "MessageDeliveryStatus" in data:
        import aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration

        out["message_delivery_status"] = (
            aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration.deserialize_json(
                data["MessageDeliveryStatus"]
            )
        )
    return out
