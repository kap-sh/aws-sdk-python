"""Generated from Smithy shape ``com.amazonaws.cloudfront#DisassociateDistributionWebACLResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DisassociateDistributionWebACLResult(TypedDict, closed=True):
    id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the distribution.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DisassociateDistributionWebACLResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])


def deserialize_xml(el: Element) -> DisassociateDistributionWebACLResult:
    out: DisassociateDistributionWebACLResult = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    return out
