"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ListRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>"""
    page_size: NotRequired["int"]
    """<p>The number of resources in the paginated list. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRequest:
    out: ListRequest = {}  # type: ignore[typeddict-item]
    return out
