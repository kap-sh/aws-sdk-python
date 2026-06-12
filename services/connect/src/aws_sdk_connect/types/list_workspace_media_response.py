"""Generated from Smithy shape ``com.amazonaws.connect#ListWorkspaceMediaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.media_list


class ListWorkspaceMediaResponse(TypedDict):
    media: NotRequired["aws_sdk_connect.types.media_list.MediaList"]
    """<p>A list of media assets for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceMediaResponse) -> dict:
    out: dict = {}
    if "media" in value:
        import aws_sdk_connect.types.media_list

        out["Media"] = aws_sdk_connect.types.media_list.serialize_json(value["media"])
    return out


def deserialize_json(data: dict) -> ListWorkspaceMediaResponse:
    out: ListWorkspaceMediaResponse = {}  # type: ignore[typeddict-item]
    if "Media" in data:
        import aws_sdk_connect.types.media_list

        out["media"] = aws_sdk_connect.types.media_list.deserialize_json(data["Media"])
    return out
