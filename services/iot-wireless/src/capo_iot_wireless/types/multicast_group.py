"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_arn
    import capo_iot_wireless.types.multicast_group_id
    import capo_iot_wireless.types.multicast_group_name


class MulticastGroup(TypedDict, closed=True):
    id: NotRequired["capo_iot_wireless.types.multicast_group_id.MulticastGroupId"]
    arn: NotRequired["capo_iot_wireless.types.multicast_group_arn.MulticastGroupArn"]
    name: NotRequired["capo_iot_wireless.types.multicast_group_name.MulticastGroupName"]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> MulticastGroup:
    out: MulticastGroup = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
