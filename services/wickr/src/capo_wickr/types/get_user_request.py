"""Generated from Smithy shape ``com.amazonaws.wickr#GetUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wickr.types.network_id
    import capo_wickr.types.user_id


class GetUserRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the user.</p>"""
    user_id: "capo_wickr.types.user_id.UserId"
    """<p>The unique identifier of the user to retrieve.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time for filtering the user's last activity. Only activity after this timestamp will be considered. Time is specified in epoch seconds.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time for filtering the user's last activity. Only activity before this timestamp will be considered. Time is specified in epoch seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserRequest:
    out: GetUserRequest = {}  # type: ignore[typeddict-item]
    return out
