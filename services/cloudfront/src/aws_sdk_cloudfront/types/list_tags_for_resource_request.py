"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource: "aws_sdk_cloudfront.types.resource_arn.ResourceARN"
    """<p>An ARN of a CloudFront resource.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTagsForResourceRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
