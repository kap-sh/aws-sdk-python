"""Generated from Smithy shape ``com.amazonaws.appfabric#StartUserAccessTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.user_access_tasks_list


class StartUserAccessTasksResponse(TypedDict):
    user_access_tasks_list: NotRequired[
        "aws_sdk_appfabric.types.user_access_tasks_list.UserAccessTasksList"
    ]
    """<p>Contains a list of user access task information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartUserAccessTasksResponse) -> dict:
    out: dict = {}
    if "user_access_tasks_list" in value:
        import aws_sdk_appfabric.types.user_access_tasks_list

        out["userAccessTasksList"] = (
            aws_sdk_appfabric.types.user_access_tasks_list.serialize_json(
                value["user_access_tasks_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartUserAccessTasksResponse:
    out: StartUserAccessTasksResponse = {}  # type: ignore[typeddict-item]
    if "userAccessTasksList" in data:
        import aws_sdk_appfabric.types.user_access_tasks_list

        out["user_access_tasks_list"] = (
            aws_sdk_appfabric.types.user_access_tasks_list.deserialize_json(
                data["userAccessTasksList"]
            )
        )
    return out
