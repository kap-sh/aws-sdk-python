"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sso_admin.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.validation_exception_message
    import aws_sdk_sso_admin.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_sso_admin.types.validation_exception_message.ValidationExceptionMessage"
    ]
    reason: NotRequired[
        "aws_sdk_sso_admin.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the validation exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_sso_admin.types.validation_exception_reason

        out["Reason"] = (
            aws_sdk_sso_admin.types.validation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_sso_admin.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_sso_admin.types.validation_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssoadmin#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ValidationException":
        return cls(deserialize_aws_json_1_1(data))
