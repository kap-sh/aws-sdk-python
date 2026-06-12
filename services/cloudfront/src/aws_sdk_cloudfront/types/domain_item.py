"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DomainItem(TypedDict):
    domain: "aws_sdk_cloudfront.types.string.string"
    """<p>The domain name.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DomainItem, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])


def deserialize_xml(el: Element) -> DomainItem:
    out: DomainItem = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        raise DeserializationError("DomainItem.domain required")
    return out
