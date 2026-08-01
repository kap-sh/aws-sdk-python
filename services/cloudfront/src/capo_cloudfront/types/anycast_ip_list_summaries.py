"""Generated from Smithy shape ``com.amazonaws.cloudfront#AnycastIpListSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.anycast_ip_list_summary

AnycastIpListSummaries: TypeAlias = list[
    "capo_cloudfront.types.anycast_ip_list_summary.AnycastIpListSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: AnycastIpListSummaries, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.anycast_ip_list_summary

        capo_cloudfront.types.anycast_ip_list_summary.serialize_xml(
            item, el, "AnycastIpListSummary"
        )


def deserialize_xml(el: Element) -> AnycastIpListSummaries:
    import capo_cloudfront.types.anycast_ip_list_summary

    out: AnycastIpListSummaries = []
    for child in el.findall("AnycastIpListSummary"):
        out.append(capo_cloudfront.types.anycast_ip_list_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: AnycastIpListSummaries, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.anycast_ip_list_summary

        capo_cloudfront.types.anycast_ip_list_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> AnycastIpListSummaries:
    import capo_cloudfront.types.anycast_ip_list_summary

    out: AnycastIpListSummaries = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.anycast_ip_list_summary.deserialize_xml(child))
    return out
