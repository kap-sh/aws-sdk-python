"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateMulticastGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_arn
    import capo_iot_wireless.types.multicast_group_id


class CreateMulticastGroupResponse(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.multicast_group_arn.MulticastGroupArn"]
    id: NotRequired["capo_iot_wireless.types.multicast_group_id.MulticastGroupId"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMulticastGroupResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateMulticastGroupResponse:
    out: CreateMulticastGroupResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
