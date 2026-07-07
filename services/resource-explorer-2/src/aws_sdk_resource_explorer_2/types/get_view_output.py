"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetViewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.tag_map
    import aws_sdk_resource_explorer_2.types.view


class GetViewOutput(TypedDict, closed=True):
    view: NotRequired["aws_sdk_resource_explorer_2.types.view.View"]
    """<p>A structure that contains the details for the requested view.</p>"""
    tags: NotRequired["aws_sdk_resource_explorer_2.types.tag_map.TagMap"]
    """<p>Tag key and value pairs that are attached to the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetViewOutput) -> dict:
    out: dict = {}
    if "view" in value:
        import aws_sdk_resource_explorer_2.types.view

        out["View"] = aws_sdk_resource_explorer_2.types.view.serialize_json(
            value["view"]
        )
    if "tags" in value:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["Tags"] = aws_sdk_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetViewOutput:
    out: GetViewOutput = {}  # type: ignore[typeddict-item]
    if "View" in data:
        import aws_sdk_resource_explorer_2.types.view

        out["view"] = aws_sdk_resource_explorer_2.types.view.deserialize_json(
            data["View"]
        )
    if "Tags" in data:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["tags"] = aws_sdk_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
