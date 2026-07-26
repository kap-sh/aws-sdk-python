"""Generated from Smithy shape ``com.amazonaws.wisdom#GetContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.content_data


class GetContentResponse(TypedDict, closed=True):
    content: NotRequired["capo_wisdom.types.content_data.ContentData"]
    """<p>The content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentResponse) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_wisdom.types.content_data

        out["content"] = capo_wisdom.types.content_data.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> GetContentResponse:
    out: GetContentResponse = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import capo_wisdom.types.content_data

        out["content"] = capo_wisdom.types.content_data.deserialize_json(
            data["content"]
        )
    return out
