"""Generated from Smithy shape ``com.amazonaws.launchwizard#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.tags


class TagResourceInput(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_launch_wizard.types.tags.Tags"
    """<p>One or more tags to attach to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_launch_wizard.types.tags

    out["tags"] = aws_sdk_launch_wizard.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_launch_wizard.types.tags

        out["tags"] = aws_sdk_launch_wizard.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
