"""Generated from Smithy shape ``com.amazonaws.backup#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.tags


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_backup.types.arn.ARN"
    """<p>The ARN that uniquely identifies the resource.</p>"""
    tags: "aws_sdk_backup.types.tags.Tags"
    r"""<p>Key-value pairs that are used to help organize your resources. You can assign your own metadata to the resources you create. For clarity, this is the structure to assign tags: <code>[{\"Key\":\"string\",\"Value\":\"string\"}]</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.tags

    out["Tags"] = aws_sdk_backup.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_backup.types.tags

        out["tags"] = aws_sdk_backup.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
