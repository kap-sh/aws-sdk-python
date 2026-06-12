"""Generated from Smithy shape ``com.amazonaws.cloudfront#VpcOriginSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.vpc_origin_summary

VpcOriginSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.vpc_origin_summary.VpcOriginSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: VpcOriginSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.vpc_origin_summary

        aws_sdk_cloudfront.types.vpc_origin_summary.serialize_xml(
            item, el, "VpcOriginSummary"
        )


def deserialize_xml(el: Element) -> VpcOriginSummaryList:
    import aws_sdk_cloudfront.types.vpc_origin_summary

    out: VpcOriginSummaryList = []
    for child in el.findall("VpcOriginSummary"):
        out.append(aws_sdk_cloudfront.types.vpc_origin_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: VpcOriginSummaryList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.vpc_origin_summary

        aws_sdk_cloudfront.types.vpc_origin_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> VpcOriginSummaryList:
    import aws_sdk_cloudfront.types.vpc_origin_summary

    out: VpcOriginSummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.vpc_origin_summary.deserialize_xml(child))
    return out
