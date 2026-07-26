"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_zonal_shift.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_arc_zonal_shift.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason for the validation exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_arc_zonal_shift.types.validation_exception_reason

    out["reason"] = (
        capo_arc_zonal_shift.types.validation_exception_reason.serialize_json(
            value["reason"]
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
        import capo_arc_zonal_shift.types.validation_exception_reason

        out["reason"] = (
            capo_arc_zonal_shift.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arczonalshift#ValidationException``."""

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
