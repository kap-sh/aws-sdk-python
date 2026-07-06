"""Generated from Smithy shape ``com.amazonaws.cloudfront#TestConnectionFunctionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_function_test_result


class TestConnectionFunctionResult(TypedDict, closed=True):
    connection_function_test_result: NotRequired[
        "aws_sdk_cloudfront.types.connection_function_test_result.ConnectionFunctionTestResult"
    ]
    """<p>The connection function test result.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: TestConnectionFunctionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_test_result" in value:
        import aws_sdk_cloudfront.types.connection_function_test_result

        aws_sdk_cloudfront.types.connection_function_test_result.serialize_xml(
            value["connection_function_test_result"], el, "ConnectionFunctionTestResult"
        )


def deserialize_xml(el: Element) -> TestConnectionFunctionResult:
    out: TestConnectionFunctionResult = {}  # type: ignore[typeddict-item]
    child_connection_function_test_result = el.find("ConnectionFunctionTestResult")
    if child_connection_function_test_result is not None:
        import aws_sdk_cloudfront.types.connection_function_test_result

        out["connection_function_test_result"] = (
            aws_sdk_cloudfront.types.connection_function_test_result.deserialize_xml(
                child_connection_function_test_result
            )
        )
    return out
