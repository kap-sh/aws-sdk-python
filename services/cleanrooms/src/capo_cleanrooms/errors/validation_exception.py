"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import ServiceError

if TYPE_CHECKING:
    import capo_cleanrooms.types.validation_exception_field_list
    import capo_cleanrooms.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["str"]
    reason: NotRequired[
        "capo_cleanrooms.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>A reason code for the exception.</p>"""
    field_list: NotRequired[
        "capo_cleanrooms.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>Validation errors for specific input parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "field_list" in value:
        import capo_cleanrooms.types.validation_exception_field_list

        out["fieldList"] = (
            capo_cleanrooms.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "fieldList" in data:
        import capo_cleanrooms.types.validation_exception_field_list

        out["field_list"] = (
            capo_cleanrooms.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cleanrooms#ValidationException``."""

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
