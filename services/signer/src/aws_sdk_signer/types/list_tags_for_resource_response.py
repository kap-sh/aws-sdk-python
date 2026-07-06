"""Generated from Smithy shape ``com.amazonaws.signer#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_signer.types.tag_map.TagMap"]
    """<p>A list of tags associated with the signing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_signer.types.tag_map

        out["tags"] = aws_sdk_signer.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_signer.types.tag_map

        out["tags"] = aws_sdk_signer.types.tag_map.deserialize_json(data["tags"])
    return out
