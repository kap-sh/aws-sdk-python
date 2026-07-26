"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.content_data


class UpdateContentResponse(TypedDict, closed=True):
    content: NotRequired["capo_qconnect.types.content_data.ContentData"]
    """<p>The content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContentResponse) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_qconnect.types.content_data

        out["content"] = capo_qconnect.types.content_data.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> UpdateContentResponse:
    out: UpdateContentResponse = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import capo_qconnect.types.content_data

        out["content"] = capo_qconnect.types.content_data.deserialize_json(
            data["content"]
        )
    return out
