"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_summary

FunctionSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.function_summary.FunctionSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: FunctionSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.function_summary

        aws_sdk_cloudfront.types.function_summary.serialize_xml(
            item, el, "FunctionSummary"
        )


def deserialize_xml(el: Element) -> FunctionSummaryList:
    import aws_sdk_cloudfront.types.function_summary

    out: FunctionSummaryList = []
    for child in el.findall("FunctionSummary"):
        out.append(aws_sdk_cloudfront.types.function_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: FunctionSummaryList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.function_summary

        aws_sdk_cloudfront.types.function_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> FunctionSummaryList:
    import aws_sdk_cloudfront.types.function_summary

    out: FunctionSummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.function_summary.deserialize_xml(child))
    return out
