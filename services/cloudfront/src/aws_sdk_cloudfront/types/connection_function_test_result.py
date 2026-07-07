"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionFunctionTestResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_function_summary
    import aws_sdk_cloudfront.types.function_execution_log_list
    import aws_sdk_cloudfront.types.sensitive_string_type
    import aws_sdk_cloudfront.types.string


class ConnectionFunctionTestResult(TypedDict, closed=True):
    connection_function_summary: NotRequired[
        "aws_sdk_cloudfront.types.connection_function_summary.ConnectionFunctionSummary"
    ]
    """<p>The connection function summary.</p>"""
    compute_utilization: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The connection function compute utilization.</p>"""
    connection_function_execution_logs: NotRequired[
        "aws_sdk_cloudfront.types.function_execution_log_list.FunctionExecutionLogList"
    ]
    """<p>The connection function execution logs.</p>"""
    connection_function_error_message: NotRequired[
        "aws_sdk_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>The connection function error message.</p>"""
    connection_function_output: NotRequired[
        "aws_sdk_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>The connection function output.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ConnectionFunctionTestResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_summary" in value:
        import aws_sdk_cloudfront.types.connection_function_summary

        aws_sdk_cloudfront.types.connection_function_summary.serialize_xml(
            value["connection_function_summary"], el, "ConnectionFunctionSummary"
        )
    if "compute_utilization" in value:
        SubElement(el, "ComputeUtilization").text = str(value["compute_utilization"])
    if "connection_function_execution_logs" in value:
        import aws_sdk_cloudfront.types.function_execution_log_list

        aws_sdk_cloudfront.types.function_execution_log_list.serialize_xml(
            value["connection_function_execution_logs"],
            el,
            "ConnectionFunctionExecutionLogs",
        )
    if "connection_function_error_message" in value:
        SubElement(el, "ConnectionFunctionErrorMessage").text = str(
            value["connection_function_error_message"]
        )
    if "connection_function_output" in value:
        SubElement(el, "ConnectionFunctionOutput").text = str(
            value["connection_function_output"]
        )


def deserialize_xml(el: Element) -> ConnectionFunctionTestResult:
    out: ConnectionFunctionTestResult = {}  # type: ignore[typeddict-item]
    child_connection_function_summary = el.find("ConnectionFunctionSummary")
    if child_connection_function_summary is not None:
        import aws_sdk_cloudfront.types.connection_function_summary

        out["connection_function_summary"] = (
            aws_sdk_cloudfront.types.connection_function_summary.deserialize_xml(
                child_connection_function_summary
            )
        )
    child_compute_utilization = el.find("ComputeUtilization")
    if child_compute_utilization is not None:
        out["compute_utilization"] = str(child_compute_utilization.text or "")
    child_connection_function_execution_logs = el.find(
        "ConnectionFunctionExecutionLogs"
    )
    if child_connection_function_execution_logs is not None:
        import aws_sdk_cloudfront.types.function_execution_log_list

        out["connection_function_execution_logs"] = (
            aws_sdk_cloudfront.types.function_execution_log_list.deserialize_xml(
                child_connection_function_execution_logs
            )
        )
    child_connection_function_error_message = el.find("ConnectionFunctionErrorMessage")
    if child_connection_function_error_message is not None:
        out["connection_function_error_message"] = str(
            child_connection_function_error_message.text or ""
        )
    child_connection_function_output = el.find("ConnectionFunctionOutput")
    if child_connection_function_output is not None:
        out["connection_function_output"] = str(
            child_connection_function_output.text or ""
        )
    return out
