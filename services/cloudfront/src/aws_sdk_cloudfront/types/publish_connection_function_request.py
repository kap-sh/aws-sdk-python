"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublishConnectionFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.resource_id
    import aws_sdk_cloudfront.types.string


class PublishConnectionFunctionRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.resource_id.ResourceId"
    """<p>The connection function ID.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the connection function.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PublishConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PublishConnectionFunctionRequest:
    out: PublishConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
