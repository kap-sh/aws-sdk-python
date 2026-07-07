"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListConnectionFunctionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_stage
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListConnectionFunctionsRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of connection functions that you want returned in the response.</p>"""
    stage: NotRequired["aws_sdk_cloudfront.types.function_stage.FunctionStage"]
    """<p>The connection function's stage.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListConnectionFunctionsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])
    if "stage" in value:
        import aws_sdk_cloudfront.types.function_stage

        aws_sdk_cloudfront.types.function_stage.serialize_xml(
            value["stage"], el, "Stage"
        )


def deserialize_xml(el: Element) -> ListConnectionFunctionsRequest:
    out: ListConnectionFunctionsRequest = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    child_stage = el.find("Stage")
    if child_stage is not None:
        import aws_sdk_cloudfront.types.function_stage

        out["stage"] = aws_sdk_cloudfront.types.function_stage.deserialize_xml(
            child_stage
        )
    return out
