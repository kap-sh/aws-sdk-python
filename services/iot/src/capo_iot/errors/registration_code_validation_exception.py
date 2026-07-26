"""Generated from Smithy shape ``com.amazonaws.iot#RegistrationCodeValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot.types.error_message2


class RegistrationCodeValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_iot.types.error_message2.ErrorMessage2"]
    """<p>Additional information about the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationCodeValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RegistrationCodeValidationException_:
    out: RegistrationCodeValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RegistrationCodeValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#RegistrationCodeValidationException``."""

    code: str | None = "RegistrationCodeValidationException"

    def __init__(self, data: RegistrationCodeValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RegistrationCodeValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RegistrationCodeValidationException":
        return cls(deserialize_json(data))
