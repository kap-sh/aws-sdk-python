"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublishConnectionFunctionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_function_summary


class PublishConnectionFunctionResult(TypedDict, closed=True):
    connection_function_summary: NotRequired[
        "aws_sdk_cloudfront.types.connection_function_summary.ConnectionFunctionSummary"
    ]
    """<p>The connection function summary.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PublishConnectionFunctionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_summary" in value:
        import aws_sdk_cloudfront.types.connection_function_summary

        aws_sdk_cloudfront.types.connection_function_summary.serialize_xml(
            value["connection_function_summary"], el, "ConnectionFunctionSummary"
        )


def deserialize_xml(el: Element) -> PublishConnectionFunctionResult:
    out: PublishConnectionFunctionResult = {}  # type: ignore[typeddict-item]
    child_connection_function_summary = el.find("ConnectionFunctionSummary")
    if child_connection_function_summary is not None:
        import aws_sdk_cloudfront.types.connection_function_summary

        out["connection_function_summary"] = (
            aws_sdk_cloudfront.types.connection_function_summary.deserialize_xml(
                child_connection_function_summary
            )
        )
    return out
