"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistributionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.streaming_distribution_summary

StreamingDistributionSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.streaming_distribution_summary.StreamingDistributionSummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: StreamingDistributionSummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.streaming_distribution_summary

        aws_sdk_cloudfront.types.streaming_distribution_summary.serialize_xml(
            item, el, "StreamingDistributionSummary"
        )


def deserialize_xml(el: Element) -> StreamingDistributionSummaryList:
    import aws_sdk_cloudfront.types.streaming_distribution_summary

    out: StreamingDistributionSummaryList = []
    for child in el.findall("StreamingDistributionSummary"):
        out.append(
            aws_sdk_cloudfront.types.streaming_distribution_summary.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: StreamingDistributionSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.streaming_distribution_summary

        aws_sdk_cloudfront.types.streaming_distribution_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> StreamingDistributionSummaryList:
    import aws_sdk_cloudfront.types.streaming_distribution_summary

    out: StreamingDistributionSummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.streaming_distribution_summary.deserialize_xml(
                child
            )
        )
    return out
