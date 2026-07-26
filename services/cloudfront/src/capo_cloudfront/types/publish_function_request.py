"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublishFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.function_name
    import capo_cloudfront.types.string


class PublishFunctionRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.function_name.FunctionName"
    """<p>The name of the function that you are publishing.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the function that you are publishing, which you can get using <code>DescribeFunction</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PublishFunctionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PublishFunctionRequest:
    out: PublishFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
