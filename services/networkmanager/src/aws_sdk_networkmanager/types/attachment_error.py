"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_error_code
    import aws_sdk_networkmanager.types.resource_arn
    import aws_sdk_networkmanager.types.server_side_string


class AttachmentError(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_networkmanager.types.attachment_error_code.AttachmentErrorCode"
    ]
    """<p>The error code for the attachment request. </p>"""
    message: NotRequired[
        "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The message associated with the error <code>code</code>.</p>"""
    resource_arn: NotRequired["aws_sdk_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the requested attachment resource.</p>"""
    request_id: NotRequired[
        "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The ID of the attachment request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentError) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_networkmanager.types.attachment_error_code

        out["Code"] = aws_sdk_networkmanager.types.attachment_error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> AttachmentError:
    out: AttachmentError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_networkmanager.types.attachment_error_code

        out["code"] = (
            aws_sdk_networkmanager.types.attachment_error_code.deserialize_json(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
