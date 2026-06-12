"""Generated from Smithy shape ``com.amazonaws.iotwireless#ConnectionStatusResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_resource_type_event_configuration


class ConnectionStatusResourceTypeEventConfiguration(TypedDict):
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_resource_type_event_configuration.LoRaWANConnectionStatusResourceTypeEventConfiguration"
    ]
    """<p>Connection status resource type event configuration object for enabling or disabling LoRaWAN related event topics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionStatusResourceTypeEventConfiguration) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_resource_type_event_configuration

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_resource_type_event_configuration.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectionStatusResourceTypeEventConfiguration:
    out: ConnectionStatusResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_resource_type_event_configuration

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_connection_status_resource_type_event_configuration.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
