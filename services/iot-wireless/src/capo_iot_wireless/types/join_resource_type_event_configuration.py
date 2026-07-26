"""Generated from Smithy shape ``com.amazonaws.iotwireless#JoinResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration


class JoinResourceTypeEventConfiguration(TypedDict, closed=True):
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration.LoRaWANJoinResourceTypeEventConfiguration"
    ]
    """<p>Join resource type event configuration object for enabling or disabling LoRaWAN related event topics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinResourceTypeEventConfiguration) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> JoinResourceTypeEventConfiguration:
    out: JoinResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_join_resource_type_event_configuration.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
