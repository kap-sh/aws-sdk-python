"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.profile_validation_error_reason


class ErrorDetail(TypedDict):
    locale: "str"
    """<p>The locale or language code for the error message.</p>"""
    message: "str"
    """<p>A human-readable description of the error.</p>"""
    reason: "aws_sdk_partnercentral_account.types.profile_validation_error_reason.ProfileValidationErrorReason"
    """<p>A machine-readable code or reason for the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorDetail) -> dict:
    out: dict = {}
    out["Locale"] = value["locale"]
    out["Message"] = value["message"]
    import aws_sdk_partnercentral_account.types.profile_validation_error_reason

    out["Reason"] = (
        aws_sdk_partnercentral_account.types.profile_validation_error_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "Locale" in data:
        out["locale"] = data["Locale"]
    else:
        raise DeserializationError("ErrorDetail.locale required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ErrorDetail.message required")
    if "Reason" in data:
        import aws_sdk_partnercentral_account.types.profile_validation_error_reason

        out["reason"] = (
            aws_sdk_partnercentral_account.types.profile_validation_error_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ErrorDetail.reason required")
    return out
