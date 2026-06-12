"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedSecurityControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.unprocessed_error_code


class UnprocessedSecurityControl(TypedDict):
    security_control_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) for which a response couldn't be returned. </p>"""
    error_code: NotRequired[
        "aws_sdk_securityhub.types.unprocessed_error_code.UnprocessedErrorCode"
    ]
    """<p> The error code for the unprocessed security control. The <code>NOT_FOUND</code> value has been deprecated and replaced by the <code>RESOURCE_NOT_FOUND</code> value. </p>"""
    error_reason: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The reason why the security control was unprocessed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedSecurityControl) -> dict:
    out: dict = {}
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "error_code" in value:
        import aws_sdk_securityhub.types.unprocessed_error_code

        out["ErrorCode"] = (
            aws_sdk_securityhub.types.unprocessed_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_reason" in value:
        out["ErrorReason"] = value["error_reason"]
    return out


def deserialize_json(data: dict) -> UnprocessedSecurityControl:
    out: UnprocessedSecurityControl = {}  # type: ignore[typeddict-item]
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "ErrorCode" in data:
        import aws_sdk_securityhub.types.unprocessed_error_code

        out["error_code"] = (
            aws_sdk_securityhub.types.unprocessed_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if "ErrorReason" in data:
        out["error_reason"] = data["ErrorReason"]
    return out
