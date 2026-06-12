"""Generated from Smithy shape ``com.amazonaws.cloudfront#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.resource_arn
    import aws_sdk_cloudfront.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource: "aws_sdk_cloudfront.types.resource_arn.ResourceARN"
    """<p>An ARN of a CloudFront resource.</p>"""
    tag_keys: "aws_sdk_cloudfront.types.tag_keys.TagKeys"
    """<p>A complex type that contains zero or more <code>Tag</code> key elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UntagResourceRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.tag_keys

    aws_sdk_cloudfront.types.tag_keys.serialize_xml(value["tag_keys"], el, "TagKeys")


def deserialize_xml(el: Element) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_cloudfront.types.tag_keys

        out["tag_keys"] = aws_sdk_cloudfront.types.tag_keys.deserialize_xml(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
