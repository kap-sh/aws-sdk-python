"""Generated from Smithy shape ``com.amazonaws.swf#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.arn
    import aws_sdk_swf.types.resource_tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_swf.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the Amazon SWF domain.</p>"""
    tags: "aws_sdk_swf.types.resource_tag_list.ResourceTagList"
    """<p>The list of tags to add to a domain. </p> <p>Tags may only contain unicode letters, digits, whitespace, or these symbols: <code>_ . : / = + - @</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_swf.types.resource_tag_list

    out["tags"] = aws_sdk_swf.types.resource_tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "tags" in data:
        import aws_sdk_swf.types.resource_tag_list

        out["tags"] = aws_sdk_swf.types.resource_tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
