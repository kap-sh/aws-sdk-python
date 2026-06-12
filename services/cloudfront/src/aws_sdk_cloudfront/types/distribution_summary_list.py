"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_summary

DistributionSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.distribution_summary.DistributionSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: DistributionSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.distribution_summary

        aws_sdk_cloudfront.types.distribution_summary.serialize_xml(
            item, el, "DistributionSummary"
        )


def deserialize_xml(el: Element) -> DistributionSummaryList:
    import aws_sdk_cloudfront.types.distribution_summary

    out: DistributionSummaryList = []
    for child in el.findall("DistributionSummary"):
        out.append(aws_sdk_cloudfront.types.distribution_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: DistributionSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.distribution_summary

        aws_sdk_cloudfront.types.distribution_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> DistributionSummaryList:
    import aws_sdk_cloudfront.types.distribution_summary

    out: DistributionSummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.distribution_summary.deserialize_xml(child))
    return out
