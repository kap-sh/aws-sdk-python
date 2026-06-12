"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFunctionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_summary
    import aws_sdk_cloudfront.types.string


class CreateFunctionResult(TypedDict):
    function_summary: NotRequired[
        "aws_sdk_cloudfront.types.function_summary.FunctionSummary"
    ]
    """<p>Contains configuration information and metadata about a CloudFront function.</p>"""
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The URL of the CloudFront function. Use the URL to manage the function with the CloudFront API.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the CloudFront function.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateFunctionResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "function_summary" in value:
        import aws_sdk_cloudfront.types.function_summary

        aws_sdk_cloudfront.types.function_summary.serialize_xml(
            value["function_summary"], el, "FunctionSummary"
        )


def deserialize_xml(el: Element) -> CreateFunctionResult:
    out: CreateFunctionResult = {}  # type: ignore[typeddict-item]
    child_function_summary = el.find("FunctionSummary")
    if child_function_summary is not None:
        import aws_sdk_cloudfront.types.function_summary

        out["function_summary"] = (
            aws_sdk_cloudfront.types.function_summary.deserialize_xml(
                child_function_summary
            )
        )
    return out
