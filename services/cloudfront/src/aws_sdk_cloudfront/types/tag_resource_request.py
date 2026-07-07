"""Generated from Smithy shape ``com.amazonaws.cloudfront#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.resource_arn
    import aws_sdk_cloudfront.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource: "aws_sdk_cloudfront.types.resource_arn.ResourceARN"
    """<p>An ARN of a CloudFront resource.</p>"""
    tags: "aws_sdk_cloudfront.types.tags.Tags"
    """<p>A complex type that contains zero or more <code>Tag</code> elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TagResourceRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.tags

    aws_sdk_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudfront.types.tags

        out["tags"] = aws_sdk_cloudfront.types.tags.deserialize_xml(child_tags)
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
