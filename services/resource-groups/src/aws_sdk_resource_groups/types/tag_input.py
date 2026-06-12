"""Generated from Smithy shape ``com.amazonaws.resourcegroups#TagInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_arn_v2
    import aws_sdk_resource_groups.types.tags


class TagInput(TypedDict):
    arn: "aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"
    """<p>The Amazon resource name (ARN) of the resource group to which to add tags.</p>"""
    tags: "aws_sdk_resource_groups.types.tags.Tags"
    """<p>The tags to add to the specified resource group. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagInput) -> dict:
    out: dict = {}
    import aws_sdk_resource_groups.types.tags

    out["Tags"] = aws_sdk_resource_groups.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagInput:
    out: TagInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_resource_groups.types.tags

        out["tags"] = aws_sdk_resource_groups.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagInput.tags required")
    return out
