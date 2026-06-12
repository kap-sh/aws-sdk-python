"""Generated from Smithy shape ``com.amazonaws.s3control#AsyncOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.async_creation_timestamp
    import aws_sdk_s3_control.types.async_operation_name
    import aws_sdk_s3_control.types.async_request_parameters
    import aws_sdk_s3_control.types.async_request_status
    import aws_sdk_s3_control.types.async_request_token_arn
    import aws_sdk_s3_control.types.async_response_details


class AsyncOperation(TypedDict):
    creation_time: NotRequired[
        "aws_sdk_s3_control.types.async_creation_timestamp.AsyncCreationTimestamp"
    ]
    """<p>The time that the request was sent to the service.</p>"""
    operation: NotRequired[
        "aws_sdk_s3_control.types.async_operation_name.AsyncOperationName"
    ]
    """<p>The specific operation for the asynchronous request.</p>"""
    request_token_arn: NotRequired[
        "aws_sdk_s3_control.types.async_request_token_arn.AsyncRequestTokenARN"
    ]
    """<p>The request token associated with the request.</p>"""
    request_parameters: NotRequired[
        "aws_sdk_s3_control.types.async_request_parameters.AsyncRequestParameters"
    ]
    """<p>The parameters associated with the request.</p>"""
    request_status: NotRequired[
        "aws_sdk_s3_control.types.async_request_status.AsyncRequestStatus"
    ]
    """<p>The current status of the request.</p>"""
    response_details: NotRequired[
        "aws_sdk_s3_control.types.async_response_details.AsyncResponseDetails"
    ]
    """<p>The details of the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AsyncOperation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "creation_time" in value:
        import aws_sdk_s3_control.types.async_creation_timestamp

        aws_sdk_s3_control.types.async_creation_timestamp.serialize_xml(
            value["creation_time"], el, "CreationTime"
        )
    if "operation" in value:
        import aws_sdk_s3_control.types.async_operation_name

        aws_sdk_s3_control.types.async_operation_name.serialize_xml(
            value["operation"], el, "Operation"
        )
    if "request_token_arn" in value:
        SubElement(el, "RequestTokenARN").text = str(value["request_token_arn"])
    if "request_parameters" in value:
        import aws_sdk_s3_control.types.async_request_parameters

        aws_sdk_s3_control.types.async_request_parameters.serialize_xml(
            value["request_parameters"], el, "RequestParameters"
        )
    if "request_status" in value:
        SubElement(el, "RequestStatus").text = str(value["request_status"])
    if "response_details" in value:
        import aws_sdk_s3_control.types.async_response_details

        aws_sdk_s3_control.types.async_response_details.serialize_xml(
            value["response_details"], el, "ResponseDetails"
        )


def deserialize_xml(el: Element) -> AsyncOperation:
    out: AsyncOperation = {}  # type: ignore[typeddict-item]
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_s3_control.types.async_creation_timestamp

        out["creation_time"] = (
            aws_sdk_s3_control.types.async_creation_timestamp.deserialize_xml(
                child_creation_time
            )
        )
    child_operation = el.find("Operation")
    if child_operation is not None:
        import aws_sdk_s3_control.types.async_operation_name

        out["operation"] = (
            aws_sdk_s3_control.types.async_operation_name.deserialize_xml(
                child_operation
            )
        )
    child_request_token_arn = el.find("RequestTokenARN")
    if child_request_token_arn is not None:
        out["request_token_arn"] = str(child_request_token_arn.text or "")
    child_request_parameters = el.find("RequestParameters")
    if child_request_parameters is not None:
        import aws_sdk_s3_control.types.async_request_parameters

        out["request_parameters"] = (
            aws_sdk_s3_control.types.async_request_parameters.deserialize_xml(
                child_request_parameters
            )
        )
    child_request_status = el.find("RequestStatus")
    if child_request_status is not None:
        out["request_status"] = str(child_request_status.text or "")
    child_response_details = el.find("ResponseDetails")
    if child_response_details is not None:
        import aws_sdk_s3_control.types.async_response_details

        out["response_details"] = (
            aws_sdk_s3_control.types.async_response_details.deserialize_xml(
                child_response_details
            )
        )
    return out
