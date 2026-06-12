"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateMulticastGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.lo_ra_wan_multicast
    import aws_sdk_iot_wireless.types.multicast_group_id
    import aws_sdk_iot_wireless.types.multicast_group_name


class UpdateMulticastGroupRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"
    name: NotRequired[
        "aws_sdk_iot_wireless.types.multicast_group_name.MulticastGroupName"
    ]
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_multicast.LoRaWANMulticast"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMulticastGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast

        out["LoRaWAN"] = aws_sdk_iot_wireless.types.lo_ra_wan_multicast.serialize_json(
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
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_multicast.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
