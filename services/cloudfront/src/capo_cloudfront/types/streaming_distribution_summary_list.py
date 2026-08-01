"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistributionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.streaming_distribution_summary

StreamingDistributionSummaryList: TypeAlias = list[
    "capo_cloudfront.types.streaming_distribution_summary.StreamingDistributionSummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: StreamingDistributionSummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.streaming_distribution_summary

        capo_cloudfront.types.streaming_distribution_summary.serialize_xml(
            item, el, "StreamingDistributionSummary"
        )


def deserialize_xml(el: Element) -> StreamingDistributionSummaryList:
    import capo_cloudfront.types.streaming_distribution_summary

    out: StreamingDistributionSummaryList = []
    for child in el.findall("StreamingDistributionSummary"):
        out.append(
            capo_cloudfront.types.streaming_distribution_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: StreamingDistributionSummaryList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.streaming_distribution_summary

        capo_cloudfront.types.streaming_distribution_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> StreamingDistributionSummaryList:
    import capo_cloudfront.types.streaming_distribution_summary

    out: StreamingDistributionSummaryList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.streaming_distribution_summary.deserialize_xml(child)
        )
    return out
