"""Generated from Smithy shape ``com.amazonaws.connect#GetCurrentUserDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token
    import capo_connect.types.user_data_list


class GetCurrentUserDataResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    user_data_list: NotRequired["capo_connect.types.user_data_list.UserDataList"]
    """<p>A list of the user data that is returned.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total count of the result, regardless of the current page size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCurrentUserDataResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "user_data_list" in value:
        import capo_connect.types.user_data_list

        out["UserDataList"] = capo_connect.types.user_data_list.serialize_json(
            value["user_data_list"]
        )
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> GetCurrentUserDataResponse:
    out: GetCurrentUserDataResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "UserDataList" in data:
        import capo_connect.types.user_data_list

        out["user_data_list"] = capo_connect.types.user_data_list.deserialize_json(
            data["UserDataList"]
        )
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
