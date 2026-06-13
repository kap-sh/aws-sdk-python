"""Generated from Smithy shape ``com.amazonaws.securitylake#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.amazon_resource_name
    import aws_sdk_securitylake.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource to add or update the tags for.</p>"""
    tags: "aws_sdk_securitylake.types.tag_list.TagList"
    """<p>An array of objects, one for each tag (key and value) to associate with the Amazon Security Lake resource. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_securitylake.types.tag_list

    out["tags"] = aws_sdk_securitylake.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_securitylake.types.tag_list

        out["tags"] = aws_sdk_securitylake.types.tag_list.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
