"""Generated from Smithy shape ``com.amazonaws.swf#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.arn
    import aws_sdk_swf.types.resource_tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_swf.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the Amazon SWF domain.</p>"""
    tag_keys: "aws_sdk_swf.types.resource_tag_key_list.ResourceTagKeyList"
    """<p>The list of tags to remove from the Amazon SWF domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_swf.types.resource_tag_key_list

    out["tagKeys"] = aws_sdk_swf.types.resource_tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_swf.types.resource_tag_key_list

        out["tag_keys"] = (
            aws_sdk_swf.types.resource_tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
