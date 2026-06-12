"""Generated from Smithy shape ``com.amazonaws.iotwireless#JoinResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration


class JoinResourceTypeEventConfiguration(TypedDict):
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration.LoRaWANJoinResourceTypeEventConfiguration"
    ]
    """<p>Join resource type event configuration object for enabling or disabling LoRaWAN related event topics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinResourceTypeEventConfiguration) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> JoinResourceTypeEventConfiguration:
    out: JoinResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
