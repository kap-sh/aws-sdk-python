"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionResourceId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DistributionResourceId(TypedDict, closed=True):
    distribution_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the multi-tenant distribution.</p>"""
    distribution_tenant_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionResourceId, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "distribution_id" in value:
        SubElement(el, "DistributionId").text = str(value["distribution_id"])
    if "distribution_tenant_id" in value:
        SubElement(el, "DistributionTenantId").text = str(
            value["distribution_tenant_id"]
        )


def deserialize_xml(el: Element) -> DistributionResourceId:
    out: DistributionResourceId = {}  # type: ignore[typeddict-item]
    child_distribution_id = el.find("DistributionId")
    if child_distribution_id is not None:
        out["distribution_id"] = str(child_distribution_id.text or "")
    child_distribution_tenant_id = el.find("DistributionTenantId")
    if child_distribution_tenant_id is not None:
        out["distribution_tenant_id"] = str(child_distribution_tenant_id.text or "")
    return out
