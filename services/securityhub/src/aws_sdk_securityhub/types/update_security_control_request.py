"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateSecurityControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.alpha_numeric_non_empty_string
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.parameters


class UpdateSecurityControlRequest(TypedDict, closed=True):
    security_control_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) or ID of the control to update. </p>"""
    parameters: NotRequired["aws_sdk_securityhub.types.parameters.Parameters"]
    """<p> An object that specifies which security control parameters to update. </p>"""
    last_update_reason: NotRequired[
        "aws_sdk_securityhub.types.alpha_numeric_non_empty_string.AlphaNumericNonEmptyString"
    ]
    """<p> The most recent reason for updating the properties of the security control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityControlRequest) -> dict:
    out: dict = {}
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "parameters" in value:
        import aws_sdk_securityhub.types.parameters

        out["Parameters"] = aws_sdk_securityhub.types.parameters.serialize_json(
            value["parameters"]
        )
    if "last_update_reason" in value:
        out["LastUpdateReason"] = value["last_update_reason"]
    return out


def deserialize_json(data: dict) -> UpdateSecurityControlRequest:
    out: UpdateSecurityControlRequest = {}  # type: ignore[typeddict-item]
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "Parameters" in data:
        import aws_sdk_securityhub.types.parameters

        out["parameters"] = aws_sdk_securityhub.types.parameters.deserialize_json(
            data["Parameters"]
        )
    if "LastUpdateReason" in data:
        out["last_update_reason"] = data["LastUpdateReason"]
    return out
