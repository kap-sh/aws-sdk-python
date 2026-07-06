"""Generated from Smithy shape ``com.amazonaws.cloudfront#DisassociateDistributionTenantWebACLResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DisassociateDistributionTenantWebACLResult(TypedDict, closed=True):
    id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The ID of the distribution tenant.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DisassociateDistributionTenantWebACLResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])


def deserialize_xml(el: Element) -> DisassociateDistributionTenantWebACLResult:
    out: DisassociateDistributionTenantWebACLResult = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    return out
