"""Generated from Smithy shape ``com.amazonaws.appmesh#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.arn
    import aws_sdk_app_mesh.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_app_mesh.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>"""
    tags: "aws_sdk_app_mesh.types.tag_list.TagList"
    """<p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.tag_list

    out["tags"] = aws_sdk_app_mesh.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_app_mesh.types.tag_list

        out["tags"] = aws_sdk_app_mesh.types.tag_list.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
