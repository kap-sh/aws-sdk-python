"""Generated from Smithy shape ``com.amazonaws.connect#ListWorkspaceMediaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.media_list


class ListWorkspaceMediaResponse(TypedDict, closed=True):
    media: NotRequired["capo_connect.types.media_list.MediaList"]
    """<p>A list of media assets for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceMediaResponse) -> dict:
    out: dict = {}
    if "media" in value:
        import capo_connect.types.media_list

        out["Media"] = capo_connect.types.media_list.serialize_json(value["media"])
    return out


def deserialize_json(data: dict) -> ListWorkspaceMediaResponse:
    out: ListWorkspaceMediaResponse = {}  # type: ignore[typeddict-item]
    if "Media" in data:
        import capo_connect.types.media_list

        out["media"] = capo_connect.types.media_list.deserialize_json(data["Media"])
    return out
