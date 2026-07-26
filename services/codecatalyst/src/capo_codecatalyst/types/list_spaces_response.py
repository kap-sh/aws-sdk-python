"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSpacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.space_summaries


class ListSpacesResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    items: NotRequired["capo_codecatalyst.types.space_summaries.SpaceSummaries"]
    """<p>Information about the spaces. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpacesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import capo_codecatalyst.types.space_summaries

        out["items"] = capo_codecatalyst.types.space_summaries.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> ListSpacesResponse:
    out: ListSpacesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import capo_codecatalyst.types.space_summaries

        out["items"] = capo_codecatalyst.types.space_summaries.deserialize_json(
            data["items"]
        )
    return out
