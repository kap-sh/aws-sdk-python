"""Generated from Smithy shape ``com.amazonaws.iot#ListThingRegistrationTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.task_id_list


class ListThingRegistrationTasksResponse(TypedDict, closed=True):
    task_ids: NotRequired["capo_iot.types.task_id_list.TaskIdList"]
    """<p>A list of bulk thing provisioning task IDs.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingRegistrationTasksResponse) -> dict:
    out: dict = {}
    if "task_ids" in value:
        import capo_iot.types.task_id_list

        out["taskIds"] = capo_iot.types.task_id_list.serialize_json(value["task_ids"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingRegistrationTasksResponse:
    out: ListThingRegistrationTasksResponse = {}  # type: ignore[typeddict-item]
    if "taskIds" in data:
        import capo_iot.types.task_id_list

        out["task_ids"] = capo_iot.types.task_id_list.deserialize_json(data["taskIds"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
