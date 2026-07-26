"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateMulticastGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.lo_ra_wan_multicast
    import capo_iot_wireless.types.multicast_group_id
    import capo_iot_wireless.types.multicast_group_name


class UpdateMulticastGroupRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"
    name: NotRequired["capo_iot_wireless.types.multicast_group_name.MulticastGroupName"]
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_multicast.LoRaWANMulticast"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMulticastGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_multicast

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_multicast.serialize_json(
            value["lo_ra_wan"]
        )
    return out


def deserialize_json(data: dict) -> UpdateMulticastGroupRequest:
    out: UpdateMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_multicast

        out["lo_ra_wan"] = capo_iot_wireless.types.lo_ra_wan_multicast.deserialize_json(
            data["LoRaWAN"]
        )
    return out
