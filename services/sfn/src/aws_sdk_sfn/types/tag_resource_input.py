"""Generated from Smithy shape ``com.amazonaws.sfn#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.tag_list


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the Step Functions state machine or activity.</p>"""
    tags: "aws_sdk_sfn.types.tag_list.TagList"
    """<p>The list of tags to add to a resource.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_sfn.types.tag_list

    out["tags"] = aws_sdk_sfn.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "tags" in data:
        import aws_sdk_sfn.types.tag_list

        out["tags"] = aws_sdk_sfn.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
