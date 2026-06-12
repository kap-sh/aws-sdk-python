"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.arn
    import aws_sdk_socialmessaging.types.string_list


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_socialmessaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "aws_sdk_socialmessaging.types.string_list.StringList"
    """<p>The keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_socialmessaging.types.string_list

    out["tagKeys"] = aws_sdk_socialmessaging.types.string_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_socialmessaging.types.string_list

        out["tag_keys"] = aws_sdk_socialmessaging.types.string_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
