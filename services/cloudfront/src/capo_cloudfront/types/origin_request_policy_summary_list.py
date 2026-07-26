"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_request_policy_summary

OriginRequestPolicySummaryList: TypeAlias = list[
    "capo_cloudfront.types.origin_request_policy_summary.OriginRequestPolicySummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: OriginRequestPolicySummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.origin_request_policy_summary

        capo_cloudfront.types.origin_request_policy_summary.serialize_xml(
            item, el, "OriginRequestPolicySummary"
        )


def deserialize_xml(el: Element) -> OriginRequestPolicySummaryList:
    import capo_cloudfront.types.origin_request_policy_summary

    out: OriginRequestPolicySummaryList = []
    for child in el.findall("OriginRequestPolicySummary"):
        out.append(
            capo_cloudfront.types.origin_request_policy_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: OriginRequestPolicySummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.origin_request_policy_summary

        capo_cloudfront.types.origin_request_policy_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> OriginRequestPolicySummaryList:
    import capo_cloudfront.types.origin_request_policy_summary

    out: OriginRequestPolicySummaryList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.origin_request_policy_summary.deserialize_xml(child)
        )
    return out
