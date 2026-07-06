"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_name
    import aws_sdk_cloudfront.types.function_stage


class GetFunctionRequest(TypedDict, closed=True):
    name: "aws_sdk_cloudfront.types.function_name.FunctionName"
    """<p>The name of the function whose code you are getting.</p>"""
    stage: NotRequired["aws_sdk_cloudfront.types.function_stage.FunctionStage"]
    """<p>The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetFunctionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetFunctionRequest:
    out: GetFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
