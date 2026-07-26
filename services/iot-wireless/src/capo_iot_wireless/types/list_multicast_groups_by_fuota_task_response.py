"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListMulticastGroupsByFuotaTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_list_by_fuota_task
    import capo_iot_wireless.types.next_token


class ListMulticastGroupsByFuotaTaskResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    multicast_group_list: NotRequired[
        "capo_iot_wireless.types.multicast_group_list_by_fuota_task.MulticastGroupListByFuotaTask"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListMulticastGroupsByFuotaTaskResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multicast_group_list" in value:
        import capo_iot_wireless.types.multicast_group_list_by_fuota_task

        out["MulticastGroupList"] = (
            capo_iot_wireless.types.multicast_group_list_by_fuota_task.serialize_json(
                value["multicast_group_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListMulticastGroupsByFuotaTaskResponse:
    out: ListMulticastGroupsByFuotaTaskResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MulticastGroupList" in data:
        import capo_iot_wireless.types.multicast_group_list_by_fuota_task

        out["multicast_group_list"] = (
            capo_iot_wireless.types.multicast_group_list_by_fuota_task.deserialize_json(
                data["MulticastGroupList"]
            )
        )
    return out
