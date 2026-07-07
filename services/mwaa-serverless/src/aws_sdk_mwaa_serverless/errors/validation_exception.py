"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mwaa_serverless.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.error_message
    import aws_sdk_mwaa_serverless.types.validation_exception_fields
    import aws_sdk_mwaa_serverless.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "aws_sdk_mwaa_serverless.types.error_message.ErrorMessage"
    reason: "aws_sdk_mwaa_serverless.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason the request failed validation.</p>"""
    field_list: NotRequired[
        "aws_sdk_mwaa_serverless.types.validation_exception_fields.ValidationExceptionFields"
    ]
    """<p>The fields that failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import aws_sdk_mwaa_serverless.types.validation_exception_reason

    out["Reason"] = (
        aws_sdk_mwaa_serverless.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "field_list" in value:
        import aws_sdk_mwaa_serverless.types.validation_exception_fields

        out["FieldList"] = (
            aws_sdk_mwaa_serverless.types.validation_exception_fields.serialize_aws_json_1_0(
                value["field_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "Reason" in data:
        import aws_sdk_mwaa_serverless.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_mwaa_serverless.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "FieldList" in data:
        import aws_sdk_mwaa_serverless.types.validation_exception_fields

        out["field_list"] = (
            aws_sdk_mwaa_serverless.types.validation_exception_fields.deserialize_aws_json_1_0(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mwaaserverless#ValidationException``."""

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
