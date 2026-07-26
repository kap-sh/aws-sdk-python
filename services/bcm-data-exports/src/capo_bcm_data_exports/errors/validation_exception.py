"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_data_exports.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.generic_string
    import capo_bcm_data_exports.types.validation_exception_field_list
    import capo_bcm_data_exports.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_bcm_data_exports.types.generic_string.GenericString"
    reason: NotRequired[
        "capo_bcm_data_exports.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the validation exception.</p>"""
    fields: NotRequired[
        "capo_bcm_data_exports.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The list of fields that are invalid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import capo_bcm_data_exports.types.validation_exception_reason

        out["Reason"] = (
            capo_bcm_data_exports.types.validation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "fields" in value:
        import capo_bcm_data_exports.types.validation_exception_field_list

        out["Fields"] = (
            capo_bcm_data_exports.types.validation_exception_field_list.serialize_aws_json_1_1(
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
        import capo_bcm_data_exports.types.validation_exception_reason

        out["reason"] = (
            capo_bcm_data_exports.types.validation_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    if "Fields" in data:
        import capo_bcm_data_exports.types.validation_exception_field_list

        out["fields"] = (
            capo_bcm_data_exports.types.validation_exception_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmdataexports#ValidationException``."""

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
