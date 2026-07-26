"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastGroupByFuotaTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_id


class MulticastGroupByFuotaTask(TypedDict, closed=True):
    id: NotRequired["capo_iot_wireless.types.multicast_group_id.MulticastGroupId"]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastGroupByFuotaTask) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> MulticastGroupByFuotaTask:
    out: MulticastGroupByFuotaTask = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
