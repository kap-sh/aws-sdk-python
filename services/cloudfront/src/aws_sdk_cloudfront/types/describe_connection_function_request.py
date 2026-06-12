"""Generated from Smithy shape ``com.amazonaws.cloudfront#DescribeConnectionFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_stage
    import aws_sdk_cloudfront.types.string


class DescribeConnectionFunctionRequest(TypedDict):
    identifier: "aws_sdk_cloudfront.types.string.string"
    """<p>The connection function's identifier.</p>"""
    stage: NotRequired["aws_sdk_cloudfront.types.function_stage.FunctionStage"]
    """<p>The connection function's stage.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DescribeConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DescribeConnectionFunctionRequest:
    out: DescribeConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
