"""Generated from Smithy shape ``com.amazonaws.textract#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.amazon_resource_name
    import aws_sdk_textract.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_textract.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that specifies the resource to be tagged.</p>"""
    tags: "aws_sdk_textract.types.tag_map.TagMap"
    """<p>A set of tags (key-value pairs) that you want to assign to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_textract.types.tag_map

    out["Tags"] = aws_sdk_textract.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_textract.types.tag_map

        out["tags"] = aws_sdk_textract.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
