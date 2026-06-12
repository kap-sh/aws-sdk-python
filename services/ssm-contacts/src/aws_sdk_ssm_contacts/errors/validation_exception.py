"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.string
    import aws_sdk_ssm_contacts.types.validation_exception_field_list
    import aws_sdk_ssm_contacts.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "aws_sdk_ssm_contacts.types.string.String"
    reason: NotRequired[
        "aws_sdk_ssm_contacts.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """Reason the request failed validation"""
    fields: NotRequired[
        "aws_sdk_ssm_contacts.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """The fields that caused the error"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_ssm_contacts.types.validation_exception_reason

        out["Reason"] = (
            aws_sdk_ssm_contacts.types.validation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "fields" in value:
        import aws_sdk_ssm_contacts.types.validation_exception_field_list

        out["Fields"] = (
            aws_sdk_ssm_contacts.types.validation_exception_field_list.serialize_aws_json_1_1(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "Reason" in data:
        import aws_sdk_ssm_contacts.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_ssm_contacts.types.validation_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    if "Fields" in data:
        import aws_sdk_ssm_contacts.types.validation_exception_field_list

        out["fields"] = (
            aws_sdk_ssm_contacts.types.validation_exception_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmcontacts#ValidationException``."""

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
