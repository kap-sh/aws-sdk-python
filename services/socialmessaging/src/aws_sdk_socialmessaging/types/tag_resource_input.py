"""Generated from Smithy shape ``com.amazonaws.socialmessaging#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.arn
    import aws_sdk_socialmessaging.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_socialmessaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "aws_sdk_socialmessaging.types.tag_list.TagList"
    """<p>The tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_socialmessaging.types.tag_list

    out["tags"] = aws_sdk_socialmessaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "tags" in data:
        import aws_sdk_socialmessaging.types.tag_list

        out["tags"] = aws_sdk_socialmessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
