"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFunctionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_blob
    import aws_sdk_cloudfront.types.string


class GetFunctionResult(TypedDict):
    function_code: NotRequired["aws_sdk_cloudfront.types.function_blob.FunctionBlob"]
    """<p>The function code of a CloudFront function.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the CloudFront function.</p>"""
    content_type: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The content type (media type) of the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetFunctionResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "function_code" in value:
        import aws_sdk_cloudfront.types.function_blob

        aws_sdk_cloudfront.types.function_blob.serialize_xml(
            value["function_code"], el, "FunctionCode"
        )


def deserialize_xml(el: Element) -> GetFunctionResult:
    out: GetFunctionResult = {}  # type: ignore[typeddict-item]
    child_function_code = el.find("FunctionCode")
    if child_function_code is not None:
        import aws_sdk_cloudfront.types.function_blob

        out["function_code"] = aws_sdk_cloudfront.types.function_blob.deserialize_xml(
            child_function_code
        )
    return out
