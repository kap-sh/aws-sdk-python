"""Generated from Smithy shape ``com.amazonaws.cloudfront#InvalidationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.invalidation_summary

InvalidationSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.invalidation_summary.InvalidationSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: InvalidationSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.invalidation_summary

        aws_sdk_cloudfront.types.invalidation_summary.serialize_xml(
            item, el, "InvalidationSummary"
        )


def deserialize_xml(el: Element) -> InvalidationSummaryList:
    import aws_sdk_cloudfront.types.invalidation_summary

    out: InvalidationSummaryList = []
    for child in el.findall("InvalidationSummary"):
        out.append(aws_sdk_cloudfront.types.invalidation_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: InvalidationSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.invalidation_summary

        aws_sdk_cloudfront.types.invalidation_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> InvalidationSummaryList:
    import aws_sdk_cloudfront.types.invalidation_summary

    out: InvalidationSummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.invalidation_summary.deserialize_xml(child))
    return out
