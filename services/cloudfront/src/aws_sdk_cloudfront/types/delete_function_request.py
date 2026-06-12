"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_name
    import aws_sdk_cloudfront.types.string


class DeleteFunctionRequest(TypedDict):
    name: "aws_sdk_cloudfront.types.function_name.FunctionName"
    """<p>The name of the function that you are deleting.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the function that you are deleting, which you can get using <code>DescribeFunction</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteFunctionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteFunctionRequest:
    out: DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
