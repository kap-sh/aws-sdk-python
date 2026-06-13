"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.tag_map


class TagResourceInput(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the view or index that you want to attach tags to.</p>"""
    tags: NotRequired["aws_sdk_resource_explorer_2.types.tag_map.TagMap"]
    """<p>A list of tag key and value pairs that you want to attach to the specified view or index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["Tags"] = aws_sdk_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["tags"] = aws_sdk_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
