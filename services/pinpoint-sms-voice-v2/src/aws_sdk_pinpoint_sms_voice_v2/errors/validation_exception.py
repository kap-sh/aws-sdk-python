"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_field_list
    import aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: NotRequired["str"]
    reason: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""
    fields: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The field that failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "fields" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_field_list

        out["Fields"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "Fields" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_field_list

        out["fields"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ValidationException``."""

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
