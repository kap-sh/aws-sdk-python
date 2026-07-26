"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_access_control_summary

OriginAccessControlSummaryList: TypeAlias = list[
    "capo_cloudfront.types.origin_access_control_summary.OriginAccessControlSummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: OriginAccessControlSummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.origin_access_control_summary

        capo_cloudfront.types.origin_access_control_summary.serialize_xml(
            item, el, "OriginAccessControlSummary"
        )


def deserialize_xml(el: Element) -> OriginAccessControlSummaryList:
    import capo_cloudfront.types.origin_access_control_summary

    out: OriginAccessControlSummaryList = []
    for child in el.findall("OriginAccessControlSummary"):
        out.append(
            capo_cloudfront.types.origin_access_control_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: OriginAccessControlSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.origin_access_control_summary

        capo_cloudfront.types.origin_access_control_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> OriginAccessControlSummaryList:
    import capo_cloudfront.types.origin_access_control_summary

    out: OriginAccessControlSummaryList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.origin_access_control_summary.deserialize_xml(child)
        )
    return out
