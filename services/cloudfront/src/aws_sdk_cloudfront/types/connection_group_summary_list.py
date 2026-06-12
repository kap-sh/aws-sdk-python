"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_group_summary

ConnectionGroupSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.connection_group_summary.ConnectionGroupSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: ConnectionGroupSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.connection_group_summary

        aws_sdk_cloudfront.types.connection_group_summary.serialize_xml(
            item, el, "ConnectionGroupSummary"
        )


def deserialize_xml(el: Element) -> ConnectionGroupSummaryList:
    import aws_sdk_cloudfront.types.connection_group_summary

    out: ConnectionGroupSummaryList = []
    for child in el.findall("ConnectionGroupSummary"):
        out.append(
            aws_sdk_cloudfront.types.connection_group_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: ConnectionGroupSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.connection_group_summary

        aws_sdk_cloudfront.types.connection_group_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ConnectionGroupSummaryList:
    import aws_sdk_cloudfront.types.connection_group_summary

    out: ConnectionGroupSummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.connection_group_summary.deserialize_xml(child)
        )
    return out
