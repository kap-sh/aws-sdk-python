"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateStandardsControlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.control_status
    import aws_sdk_securityhub.types.non_empty_string


class UpdateStandardsControlRequest(TypedDict):
    standards_control_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the security standard control to enable or disable.</p>"""
    control_status: NotRequired[
        "aws_sdk_securityhub.types.control_status.ControlStatus"
    ]
    """<p>The updated status of the security standard control.</p>"""
    disabled_reason: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the reason why you are disabling a security standard control. If you are disabling a control, then this is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStandardsControlRequest) -> dict:
    out: dict = {}
    if "control_status" in value:
        import aws_sdk_securityhub.types.control_status

        out["ControlStatus"] = aws_sdk_securityhub.types.control_status.serialize_json(
            value["control_status"]
        )
    if "disabled_reason" in value:
        out["DisabledReason"] = value["disabled_reason"]
    return out


def deserialize_json(data: dict) -> UpdateStandardsControlRequest:
    out: UpdateStandardsControlRequest = {}  # type: ignore[typeddict-item]
    if "ControlStatus" in data:
        import aws_sdk_securityhub.types.control_status

        out["control_status"] = (
            aws_sdk_securityhub.types.control_status.deserialize_json(
                data["ControlStatus"]
            )
        )
    if "DisabledReason" in data:
        out["disabled_reason"] = data["DisabledReason"]
    return out
