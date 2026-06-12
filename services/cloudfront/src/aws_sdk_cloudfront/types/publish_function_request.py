"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublishFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_name
    import aws_sdk_cloudfront.types.string


class PublishFunctionRequest(TypedDict):
    name: "aws_sdk_cloudfront.types.function_name.FunctionName"
    """<p>The name of the function that you are publishing.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the function that you are publishing, which you can get using <code>DescribeFunction</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PublishFunctionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PublishFunctionRequest:
    out: PublishFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
