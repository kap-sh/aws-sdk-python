"""Generated from Smithy shape ``com.amazonaws.artifact#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_artifact.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_artifact.types.validation_exception_field_list
    import capo_artifact.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_artifact.types.validation_exception_reason.ValidationExceptionReason"
    """<p>Reason the request failed validation.</p>"""
    field_list: NotRequired[
        "capo_artifact.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The field that caused the error, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["reason"] = value["reason"]
    if "field_list" in value:
        import capo_artifact.types.validation_exception_field_list

        out["fieldList"] = (
            capo_artifact.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "reason" in data:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "fieldList" in data:
        import capo_artifact.types.validation_exception_field_list

        out["field_list"] = (
            capo_artifact.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.artifact#ValidationException``."""

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
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))
