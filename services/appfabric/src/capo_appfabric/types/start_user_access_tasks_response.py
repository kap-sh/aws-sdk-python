"""Generated from Smithy shape ``com.amazonaws.appfabric#StartUserAccessTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.user_access_tasks_list


class StartUserAccessTasksResponse(TypedDict, closed=True):
    user_access_tasks_list: NotRequired[
        "capo_appfabric.types.user_access_tasks_list.UserAccessTasksList"
    ]
    """<p>Contains a list of user access task information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartUserAccessTasksResponse) -> dict:
    out: dict = {}
    if "user_access_tasks_list" in value:
        import capo_appfabric.types.user_access_tasks_list

        out["userAccessTasksList"] = (
            capo_appfabric.types.user_access_tasks_list.serialize_json(
                value["user_access_tasks_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartUserAccessTasksResponse:
    out: StartUserAccessTasksResponse = {}  # type: ignore[typeddict-item]
    if "userAccessTasksList" in data:
        import capo_appfabric.types.user_access_tasks_list

        out["user_access_tasks_list"] = (
            capo_appfabric.types.user_access_tasks_list.deserialize_json(
                data["userAccessTasksList"]
            )
        )
    return out
