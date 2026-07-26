"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartMulticastGroupSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.lo_ra_wan_multicast_session
    import capo_iot_wireless.types.multicast_group_id


class StartMulticastGroupSessionRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"
    lo_ra_wan: (
        "capo_iot_wireless.types.lo_ra_wan_multicast_session.LoRaWANMulticastSession"
    )


# --- restJson1 ser/de ---
def serialize_json(value: StartMulticastGroupSessionRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.lo_ra_wan_multicast_session

    out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_multicast_session.serialize_json(
        value["lo_ra_wan"]
    )
    return out


def deserialize_json(data: dict) -> StartMulticastGroupSessionRequest:
    out: StartMulticastGroupSessionRequest = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_multicast_session

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_multicast_session.deserialize_json(
                data["LoRaWAN"]
            )
        )
    else:
        raise DeserializationError(
            "StartMulticastGroupSessionRequest.lo_ra_wan required"
        )
    return out
