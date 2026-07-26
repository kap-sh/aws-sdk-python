"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionTenantResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_tenant
    import capo_cloudfront.types.string


class GetDistributionTenantResult(TypedDict, closed=True):
    distribution_tenant: NotRequired[
        "capo_cloudfront.types.distribution_tenant.DistributionTenant"
    ]
    """<p>The distribution tenant that you retrieved.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetDistributionTenantResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_tenant" in value:
        import capo_cloudfront.types.distribution_tenant

        capo_cloudfront.types.distribution_tenant.serialize_xml(
            value["distribution_tenant"], el, "DistributionTenant"
        )


def deserialize_xml(el: Element) -> GetDistributionTenantResult:
    out: GetDistributionTenantResult = {}  # type: ignore[typeddict-item]
    child_distribution_tenant = el.find("DistributionTenant")
    if child_distribution_tenant is not None:
        import capo_cloudfront.types.distribution_tenant

        out["distribution_tenant"] = (
            capo_cloudfront.types.distribution_tenant.deserialize_xml(
                child_distribution_tenant
            )
        )
    return out
