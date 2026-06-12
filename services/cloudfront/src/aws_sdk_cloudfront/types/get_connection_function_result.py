"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetConnectionFunctionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_blob
    import aws_sdk_cloudfront.types.string


class GetConnectionFunctionResult(TypedDict):
    connection_function_code: NotRequired[
        "aws_sdk_cloudfront.types.function_blob.FunctionBlob"
    ]
    """<p>The connection function's code.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the connection function.</p>"""
    content_type: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The connection function's content type.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetConnectionFunctionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_code" in value:
        import aws_sdk_cloudfront.types.function_blob

        aws_sdk_cloudfront.types.function_blob.serialize_xml(
            value["connection_function_code"], el, "ConnectionFunctionCode"
        )


def deserialize_xml(el: Element) -> GetConnectionFunctionResult:
    out: GetConnectionFunctionResult = {}  # type: ignore[typeddict-item]
    child_connection_function_code = el.find("ConnectionFunctionCode")
    if child_connection_function_code is not None:
        import aws_sdk_cloudfront.types.function_blob

        out["connection_function_code"] = (
            aws_sdk_cloudfront.types.function_blob.deserialize_xml(
                child_connection_function_code
            )
        )
    return out
