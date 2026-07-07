"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspacesstreams.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.validation_exception_type


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>The input fails to satisfy the constraints specified by the service. Check the error details and modify your request.</p>"""
    error_code: NotRequired[
        "aws_sdk_keyspacesstreams.types.validation_exception_type.ValidationExceptionType"
    ]
    """<p>An error occurred validating your request. See the error message for details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "error_code" in value:
        import aws_sdk_keyspacesstreams.types.validation_exception_type

        out["errorCode"] = (
            aws_sdk_keyspacesstreams.types.validation_exception_type.serialize_aws_json_1_0(
                value["error_code"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "errorCode" in data:
        import aws_sdk_keyspacesstreams.types.validation_exception_type

        out["error_code"] = (
            aws_sdk_keyspacesstreams.types.validation_exception_type.deserialize_aws_json_1_0(
                data["errorCode"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.keyspacesstreams#ValidationException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ValidationException":
        return cls(deserialize_aws_json_1_0(data))
