"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateConnectionFunctionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.connection_function_summary
    import capo_cloudfront.types.string


class CreateConnectionFunctionResult(TypedDict, closed=True):
    connection_function_summary: NotRequired[
        "capo_cloudfront.types.connection_function_summary.ConnectionFunctionSummary"
    ]
    """<p>The summary for the connection function.</p>"""
    location: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The location of the connection function.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the connection function.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateConnectionFunctionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_summary" in value:
        import capo_cloudfront.types.connection_function_summary

        capo_cloudfront.types.connection_function_summary.serialize_xml(
            value["connection_function_summary"], el, "ConnectionFunctionSummary"
        )


def deserialize_xml(el: Element) -> CreateConnectionFunctionResult:
    out: CreateConnectionFunctionResult = {}  # type: ignore[typeddict-item]
    child_connection_function_summary = el.find("ConnectionFunctionSummary")
    if child_connection_function_summary is not None:
        import capo_cloudfront.types.connection_function_summary

        out["connection_function_summary"] = (
            capo_cloudfront.types.connection_function_summary.deserialize_xml(
                child_connection_function_summary
            )
        )
    return out
