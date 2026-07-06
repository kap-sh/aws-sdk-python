"""Generated from Smithy shape ``com.amazonaws.cloudfront#DescribeFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_name
    import aws_sdk_cloudfront.types.function_stage


class DescribeFunctionRequest(TypedDict, closed=True):
    name: "aws_sdk_cloudfront.types.function_name.FunctionName"
    """<p>The name of the function that you are getting information about.</p>"""
    stage: NotRequired["aws_sdk_cloudfront.types.function_stage.FunctionStage"]
    """<p>The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DescribeFunctionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DescribeFunctionRequest:
    out: DescribeFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
