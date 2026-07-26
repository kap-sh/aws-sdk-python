"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSpacesRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListSpacesRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpacesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSpacesRequest:
    out: ListSpacesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
