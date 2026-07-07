"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchCreateChannelMembershipError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.error_code
    import aws_sdk_chime_sdk_messaging.types.string


class BatchCreateChannelMembershipError(TypedDict, closed=True):
    member_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The <code>AppInstanceUserArn</code> of the member that the service couldn't add.</p>"""
    error_code: NotRequired["aws_sdk_chime_sdk_messaging.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_chime_sdk_messaging.types.string.String"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateChannelMembershipError) -> dict:
    out: dict = {}
    if "member_arn" in value:
        out["MemberArn"] = value["member_arn"]
    if "error_code" in value:
        import aws_sdk_chime_sdk_messaging.types.error_code

        out["ErrorCode"] = aws_sdk_chime_sdk_messaging.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchCreateChannelMembershipError:
    out: BatchCreateChannelMembershipError = {}  # type: ignore[typeddict-item]
    if "MemberArn" in data:
        out["member_arn"] = data["MemberArn"]
    if "ErrorCode" in data:
        import aws_sdk_chime_sdk_messaging.types.error_code

        out["error_code"] = (
            aws_sdk_chime_sdk_messaging.types.error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
