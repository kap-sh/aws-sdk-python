"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateDomainAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class UpdateDomainAssociationResult(TypedDict):
    domain: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The domain that you're moving.</p>"""
    resource_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The intended destination for the domain.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the target standard distribution or distribution tenant that was associated with the domain.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateDomainAssociationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "domain" in value:
        SubElement(el, "Domain").text = str(value["domain"])
    if "resource_id" in value:
        SubElement(el, "ResourceId").text = str(value["resource_id"])


def deserialize_xml(el: Element) -> UpdateDomainAssociationResult:
    out: UpdateDomainAssociationResult = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    return out
