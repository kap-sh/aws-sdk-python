"""Generated from Smithy shape ``com.amazonaws.shield#InvalidParameterException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_shield.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_shield.types.error_message
    import aws_sdk_shield.types.validation_exception_field_list
    import aws_sdk_shield.types.validation_exception_reason


class InvalidParameterException_(TypedDict):
    message: NotRequired["aws_sdk_shield.types.error_message.errorMessage"]
    reason: NotRequired[
        "aws_sdk_shield.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>Additional information about the exception.</p>"""
    fields: NotRequired[
        "aws_sdk_shield.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>Fields that caused the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import aws_sdk_shield.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_shield.types.validation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "fields" in value:
        import aws_sdk_shield.types.validation_exception_field_list

        out["fields"] = (
            aws_sdk_shield.types.validation_exception_field_list.serialize_aws_json_1_1(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "reason" in data:
        import aws_sdk_shield.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_shield.types.validation_exception_reason.deserialize_aws_json_1_1(
                data["reason"]
            )
        )
    if "fields" in data:
        import aws_sdk_shield.types.validation_exception_field_list

        out["fields"] = (
            aws_sdk_shield.types.validation_exception_field_list.deserialize_aws_json_1_1(
                data["fields"]
            )
        )
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(self, data: InvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidParameterException":
        return cls(deserialize_aws_json_1_1(data))
