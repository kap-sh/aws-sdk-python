"""Generated from Smithy shape ``com.amazonaws.s3control#AsyncErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.max_length1024_string


class AsyncErrorDetails(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_s3_control.types.max_length1024_string.MaxLength1024String"
    ]
    """<p>A string that uniquely identifies the error condition.</p>"""
    message: NotRequired[
        "aws_sdk_s3_control.types.max_length1024_string.MaxLength1024String"
    ]
    """<p>A generic description of the error condition in English.</p>"""
    resource: NotRequired[
        "aws_sdk_s3_control.types.max_length1024_string.MaxLength1024String"
    ]
    """<p>The identifier of the resource associated with the error.</p>"""
    request_id: NotRequired[
        "aws_sdk_s3_control.types.max_length1024_string.MaxLength1024String"
    ]
    """<p>The ID of the request associated with the error.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AsyncErrorDetails, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "code" in value:
        SubElement(el, "Code").text = str(value["code"])
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])
    if "resource" in value:
        SubElement(el, "Resource").text = str(value["resource"])
    if "request_id" in value:
        SubElement(el, "RequestId").text = str(value["request_id"])


def deserialize_xml(el: Element) -> AsyncErrorDetails:
    out: AsyncErrorDetails = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_resource = el.find("Resource")
    if child_resource is not None:
        out["resource"] = str(child_resource.text or "")
    child_request_id = el.find("RequestId")
    if child_request_id is not None:
        out["request_id"] = str(child_request_id.text or "")
    return out
