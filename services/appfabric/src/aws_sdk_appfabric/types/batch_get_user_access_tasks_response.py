"""Generated from Smithy shape ``com.amazonaws.appfabric#BatchGetUserAccessTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.user_access_results_list


class BatchGetUserAccessTasksResponse(TypedDict, closed=True):
    user_access_results_list: NotRequired[
        "aws_sdk_appfabric.types.user_access_results_list.UserAccessResultsList"
    ]
    """<p>Contains a list of user access results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetUserAccessTasksResponse) -> dict:
    out: dict = {}
    if "user_access_results_list" in value:
        import aws_sdk_appfabric.types.user_access_results_list

        out["userAccessResultsList"] = (
            aws_sdk_appfabric.types.user_access_results_list.serialize_json(
                value["user_access_results_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetUserAccessTasksResponse:
    out: BatchGetUserAccessTasksResponse = {}  # type: ignore[typeddict-item]
    if "userAccessResultsList" in data:
        import aws_sdk_appfabric.types.user_access_results_list

        out["user_access_results_list"] = (
            aws_sdk_appfabric.types.user_access_results_list.deserialize_json(
                data["userAccessResultsList"]
            )
        )
    return out
