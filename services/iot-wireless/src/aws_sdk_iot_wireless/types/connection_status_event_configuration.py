"""Generated from Smithy shape ``com.amazonaws.iotwireless#ConnectionStatusEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.event_notification_topic_status
    import aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_event_notification_configurations


class ConnectionStatusEventConfiguration(TypedDict, closed=True):
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_event_notification_configurations.LoRaWANConnectionStatusEventNotificationConfigurations"
    ]
    """<p>Connection status event configuration object for enabling or disabling LoRaWAN related event topics.</p>"""
    wireless_gateway_id_event_topic: NotRequired[
        "aws_sdk_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the wireless gateway ID connection status event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionStatusEventConfiguration) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_event_notification_configurations

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_event_notification_configurations.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "wireless_gateway_id_event_topic" in value:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["WirelessGatewayIdEventTopic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["wireless_gateway_id_event_topic"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectionStatusEventConfiguration:
    out: ConnectionStatusEventConfiguration = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_event_notification_configurations

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_event_notification_configurations.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "WirelessGatewayIdEventTopic" in data:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["wireless_gateway_id_event_topic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["WirelessGatewayIdEventTopic"]
            )
        )
    return out
