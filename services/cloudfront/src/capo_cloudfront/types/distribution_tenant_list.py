"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionTenantList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_tenant_summary

DistributionTenantList: TypeAlias = list[
    "capo_cloudfront.types.distribution_tenant_summary.DistributionTenantSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: DistributionTenantList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.distribution_tenant_summary

        capo_cloudfront.types.distribution_tenant_summary.serialize_xml(
            item, el, "DistributionTenantSummary"
        )


def deserialize_xml(el: Element) -> DistributionTenantList:
    import capo_cloudfront.types.distribution_tenant_summary

    out: DistributionTenantList = []
    for child in el.findall("DistributionTenantSummary"):
        out.append(
            capo_cloudfront.types.distribution_tenant_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: DistributionTenantList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.distribution_tenant_summary

        capo_cloudfront.types.distribution_tenant_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> DistributionTenantList:
    import capo_cloudfront.types.distribution_tenant_summary

    out: DistributionTenantList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.distribution_tenant_summary.deserialize_xml(child)
        )
    return out
