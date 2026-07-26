"""Generated from Smithy shape ``com.amazonaws.quicksight#ListUsersIndexCapacityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.user_index_capacity_list


class ListUsersIndexCapacityResponse(TypedDict, closed=True):
    users: NotRequired[
        "capo_quicksight.types.user_index_capacity_list.UserIndexCapacityList"
    ]
    """<p>The list of users with their index capacity metrics.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersIndexCapacityResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_quicksight.types.user_index_capacity_list

        out["users"] = capo_quicksight.types.user_index_capacity_list.serialize_json(
            value["users"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListUsersIndexCapacityResponse:
    out: ListUsersIndexCapacityResponse = {}  # type: ignore[typeddict-item]
    if "users" in data:
        import capo_quicksight.types.user_index_capacity_list

        out["users"] = capo_quicksight.types.user_index_capacity_list.deserialize_json(
            data["users"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    return out
