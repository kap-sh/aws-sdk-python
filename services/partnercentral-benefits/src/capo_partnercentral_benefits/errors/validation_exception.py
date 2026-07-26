"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_benefits.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.validation_exception_field_list
    import capo_partnercentral_benefits.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    """<p>A message describing the validation error.</p>"""
    reason: "capo_partnercentral_benefits.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason for the validation failure.</p>"""
    field_list: NotRequired[
        "capo_partnercentral_benefits.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of fields that failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_benefits.types.validation_exception_reason

    out["Reason"] = (
        capo_partnercentral_benefits.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "field_list" in value:
        import capo_partnercentral_benefits.types.validation_exception_field_list

        out["FieldList"] = (
            capo_partnercentral_benefits.types.validation_exception_field_list.serialize_aws_json_1_0(
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
        import capo_partnercentral_benefits.types.validation_exception_reason

        out["reason"] = (
            capo_partnercentral_benefits.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "FieldList" in data:
        import capo_partnercentral_benefits.types.validation_exception_field_list

        out["field_list"] = (
            capo_partnercentral_benefits.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralbenefits#ValidationException``."""

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
