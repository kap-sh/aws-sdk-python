"""Generated from Smithy shape ``com.amazonaws.cloudfront#DescribeConnectionFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.function_stage
    import capo_cloudfront.types.string


class DescribeConnectionFunctionRequest(TypedDict, closed=True):
    identifier: "capo_cloudfront.types.string.string"
    """<p>The connection function's identifier.</p>"""
    stage: NotRequired["capo_cloudfront.types.function_stage.FunctionStage"]
    """<p>The connection function's stage.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DescribeConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DescribeConnectionFunctionRequest:
    out: DescribeConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
