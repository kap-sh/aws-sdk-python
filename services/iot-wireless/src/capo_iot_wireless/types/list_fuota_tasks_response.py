"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListFuotaTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_list
    import capo_iot_wireless.types.next_token


class ListFuotaTasksResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    fuota_task_list: NotRequired[
        "capo_iot_wireless.types.fuota_task_list.FuotaTaskList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListFuotaTasksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "fuota_task_list" in value:
        import capo_iot_wireless.types.fuota_task_list

        out["FuotaTaskList"] = capo_iot_wireless.types.fuota_task_list.serialize_json(
            value["fuota_task_list"]
        )
    return out


def deserialize_json(data: dict) -> ListFuotaTasksResponse:
    out: ListFuotaTasksResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FuotaTaskList" in data:
        import capo_iot_wireless.types.fuota_task_list

        out["fuota_task_list"] = (
            capo_iot_wireless.types.fuota_task_list.deserialize_json(
                data["FuotaTaskList"]
            )
        )
    return out
