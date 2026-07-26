"""Generated from Smithy shape ``com.amazonaws.cloudfront#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.resource_arn
    import capo_cloudfront.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource: "capo_cloudfront.types.resource_arn.ResourceARN"
    """<p>An ARN of a CloudFront resource.</p>"""
    tags: "capo_cloudfront.types.tags.Tags"
    """<p>A complex type that contains zero or more <code>Tag</code> elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TagResourceRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.tags

    capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
