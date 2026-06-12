"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionFunctionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_function_summary

ConnectionFunctionSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.connection_function_summary.ConnectionFunctionSummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ConnectionFunctionSummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.connection_function_summary

        aws_sdk_cloudfront.types.connection_function_summary.serialize_xml(
            item, el, "ConnectionFunctionSummary"
        )


def deserialize_xml(el: Element) -> ConnectionFunctionSummaryList:
    import aws_sdk_cloudfront.types.connection_function_summary

    out: ConnectionFunctionSummaryList = []
    for child in el.findall("ConnectionFunctionSummary"):
        out.append(
            aws_sdk_cloudfront.types.connection_function_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: ConnectionFunctionSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.connection_function_summary

        aws_sdk_cloudfront.types.connection_function_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ConnectionFunctionSummaryList:
    import aws_sdk_cloudfront.types.connection_function_summary

    out: ConnectionFunctionSummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.connection_function_summary.deserialize_xml(child)
        )
    return out
