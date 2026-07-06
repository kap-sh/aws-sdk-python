"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_blob
    import aws_sdk_cloudfront.types.function_config
    import aws_sdk_cloudfront.types.function_name
    import aws_sdk_cloudfront.types.string


class UpdateFunctionRequest(TypedDict, closed=True):
    name: "aws_sdk_cloudfront.types.function_name.FunctionName"
    """<p>The name of the function that you are updating.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the function that you are updating, which you can get using <code>DescribeFunction</code>.</p>"""
    function_config: "aws_sdk_cloudfront.types.function_config.FunctionConfig"
    """<p>Configuration information about the function.</p>"""
    function_code: "aws_sdk_cloudfront.types.function_blob.FunctionBlob"
    r"""<p>The function code. For more information about writing a CloudFront function, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html\">Writing function code for CloudFront Functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateFunctionRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.function_config

    aws_sdk_cloudfront.types.function_config.serialize_xml(
        value["function_config"], el, "FunctionConfig"
    )
    import aws_sdk_cloudfront.types.function_blob

    aws_sdk_cloudfront.types.function_blob.serialize_xml(
        value["function_code"], el, "FunctionCode"
    )


def deserialize_xml(el: Element) -> UpdateFunctionRequest:
    out: UpdateFunctionRequest = {}  # type: ignore[typeddict-item]
    child_function_config = el.find("FunctionConfig")
    if child_function_config is not None:
        import aws_sdk_cloudfront.types.function_config

        out["function_config"] = (
            aws_sdk_cloudfront.types.function_config.deserialize_xml(
                child_function_config
            )
        )
    else:
        raise DeserializationError("UpdateFunctionRequest.function_config required")
    child_function_code = el.find("FunctionCode")
    if child_function_code is not None:
        import aws_sdk_cloudfront.types.function_blob

        out["function_code"] = aws_sdk_cloudfront.types.function_blob.deserialize_xml(
            child_function_code
        )
    else:
        raise DeserializationError("UpdateFunctionRequest.function_code required")
    return out
