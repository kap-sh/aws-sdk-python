"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.output_tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_managedblockchain.types.output_tag_map.OutputTagMap"]
    """<p>The tags assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_managedblockchain.types.output_tag_map

        out["Tags"] = aws_sdk_managedblockchain.types.output_tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_managedblockchain.types.output_tag_map

        out["tags"] = aws_sdk_managedblockchain.types.output_tag_map.deserialize_json(
            data["Tags"]
        )
    return out
