"""Generated from Smithy shape ``com.amazonaws.polly#UnsupportedPlsLanguageException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.error_message


class UnsupportedPlsLanguageException_(TypedDict, closed=True):
    message: NotRequired["capo_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedPlsLanguageException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedPlsLanguageException_:
    out: UnsupportedPlsLanguageException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedPlsLanguageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#UnsupportedPlsLanguageException``."""

    code: str | None = "UnsupportedPlsLanguageException"

    def __init__(self, data: UnsupportedPlsLanguageException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedPlsLanguageException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedPlsLanguageException":
        return cls(deserialize_json(data))
