"""Generated from Smithy shape ``com.amazonaws.cloudfront#AnycastIpListSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.anycast_ip_list_summary

AnycastIpListSummaries: TypeAlias = list[
    "aws_sdk_cloudfront.types.anycast_ip_list_summary.AnycastIpListSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: AnycastIpListSummaries, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.anycast_ip_list_summary

        aws_sdk_cloudfront.types.anycast_ip_list_summary.serialize_xml(
            item, el, "AnycastIpListSummary"
        )


def deserialize_xml(el: Element) -> AnycastIpListSummaries:
    import aws_sdk_cloudfront.types.anycast_ip_list_summary

    out: AnycastIpListSummaries = []
    for child in el.findall("AnycastIpListSummary"):
        out.append(
            aws_sdk_cloudfront.types.anycast_ip_list_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: AnycastIpListSummaries, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.anycast_ip_list_summary

        aws_sdk_cloudfront.types.anycast_ip_list_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> AnycastIpListSummaries:
    import aws_sdk_cloudfront.types.anycast_ip_list_summary

    out: AnycastIpListSummaries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.anycast_ip_list_summary.deserialize_xml(child)
        )
    return out
