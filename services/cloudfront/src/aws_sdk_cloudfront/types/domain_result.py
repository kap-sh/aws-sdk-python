"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.domain_status
    import aws_sdk_cloudfront.types.string


class DomainResult(TypedDict, closed=True):
    domain: "aws_sdk_cloudfront.types.string.string"
    """<p>The specified domain.</p>"""
    status: NotRequired["aws_sdk_cloudfront.types.domain_status.DomainStatus"]
    """<p>Whether the domain is active or inactive.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DomainResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    if "status" in value:
        import aws_sdk_cloudfront.types.domain_status

        aws_sdk_cloudfront.types.domain_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> DomainResult:
    out: DomainResult = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        raise DeserializationError("DomainResult.domain required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudfront.types.domain_status

        out["status"] = aws_sdk_cloudfront.types.domain_status.deserialize_xml(
            child_status
        )
    return out
