"""Generated from Smithy shape ``com.amazonaws.connect#ListUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.user_summary_list


class ListUsersResponse(TypedDict, closed=True):
    user_summary_list: NotRequired[
        "capo_connect.types.user_summary_list.UserSummaryList"
    ]
    """<p>Information about the users.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "user_summary_list" in value:
        import capo_connect.types.user_summary_list

        out["UserSummaryList"] = capo_connect.types.user_summary_list.serialize_json(
            value["user_summary_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "UserSummaryList" in data:
        import capo_connect.types.user_summary_list

        out["user_summary_list"] = (
            capo_connect.types.user_summary_list.deserialize_json(
                data["UserSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
