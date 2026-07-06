"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListFunctionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_stage
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListFunctionsRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of functions that you want in the response.</p>"""
    stage: NotRequired["aws_sdk_cloudfront.types.function_stage.FunctionStage"]
    """<p>An optional filter to return only the functions that are in the specified stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListFunctionsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListFunctionsRequest:
    out: ListFunctionsRequest = {}  # type: ignore[typeddict-item]
    return out
