"""Generated from Smithy shape ``com.amazonaws.ram#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ram.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string
    import aws_sdk_ram.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_share_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share that you want to add tags to. You must specify <i>either</i> <code>resourceShareArn</code>, or <code>resourceArn</code>, but not both.</p>"""
    tags: "aws_sdk_ram.types.tag_list.TagList"
    """<p>A list of one or more tag key and value pairs. The tag key must be present and not be an empty string. The tag value must be present but can be an empty string.</p>"""
    resource_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the managed permission that you want to add tags to. You must specify <i>either</i> <code>resourceArn</code>, or <code>resourceShareArn</code>, but not both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    import aws_sdk_ram.types.tag_list

    out["tags"] = aws_sdk_ram.types.tag_list.serialize_json(value["tags"])
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    if "tags" in data:
        import aws_sdk_ram.types.tag_list

        out["tags"] = aws_sdk_ram.types.tag_list.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out
