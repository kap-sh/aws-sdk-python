"""Generated from Smithy shape ``com.amazonaws.rum#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rum.types.arn
    import aws_sdk_rum.types.tag_map


class ListTagsForResourceResponse(TypedDict):
    resource_arn: "aws_sdk_rum.types.arn.Arn"
    """<p>The ARN of the resource that you are viewing.</p>"""
    tags: "aws_sdk_rum.types.tag_map.TagMap"
    """<p>The list of tag keys and values associated with the resource you specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_rum.types.tag_map

    out["Tags"] = aws_sdk_rum.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceResponse.resource_arn required")
    if "Tags" in data:
        import aws_sdk_rum.types.tag_map

        out["tags"] = aws_sdk_rum.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out
