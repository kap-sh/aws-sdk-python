"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListConnectionFunctionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_function_summary_list
    import aws_sdk_cloudfront.types.string


class ListConnectionFunctionsResult(TypedDict):
    next_marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Indicates the next page of connection functions. To get the next page of the list, use this value in the <code>Marker</code> field of your request.</p>"""
    connection_functions: NotRequired[
        "aws_sdk_cloudfront.types.connection_function_summary_list.ConnectionFunctionSummaryList"
    ]
    """<p>A list of connection functions.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListConnectionFunctionsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    if "connection_functions" in value:
        import aws_sdk_cloudfront.types.connection_function_summary_list

        aws_sdk_cloudfront.types.connection_function_summary_list.serialize_xml(
            value["connection_functions"], el, "ConnectionFunctions"
        )


def deserialize_xml(el: Element) -> ListConnectionFunctionsResult:
    out: ListConnectionFunctionsResult = {}  # type: ignore[typeddict-item]
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_connection_functions = el.find("ConnectionFunctions")
    if child_connection_functions is not None:
        import aws_sdk_cloudfront.types.connection_function_summary_list

        out["connection_functions"] = (
            aws_sdk_cloudfront.types.connection_function_summary_list.deserialize_xml(
                child_connection_functions
            )
        )
    return out
