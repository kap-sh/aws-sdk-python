"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_policy_summary

CachePolicySummaryList: TypeAlias = list[
    "capo_cloudfront.types.cache_policy_summary.CachePolicySummary"
]


# --- restXml ser/de ---
def serialize_xml(value: CachePolicySummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.cache_policy_summary

        capo_cloudfront.types.cache_policy_summary.serialize_xml(
            item, el, "CachePolicySummary"
        )


def deserialize_xml(el: Element) -> CachePolicySummaryList:
    import capo_cloudfront.types.cache_policy_summary

    out: CachePolicySummaryList = []
    for child in el.findall("CachePolicySummary"):
        out.append(capo_cloudfront.types.cache_policy_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: CachePolicySummaryList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.cache_policy_summary

        capo_cloudfront.types.cache_policy_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> CachePolicySummaryList:
    import capo_cloudfront.types.cache_policy_summary

    out: CachePolicySummaryList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.cache_policy_summary.deserialize_xml(child))
    return out
