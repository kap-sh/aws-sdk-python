"""Generated from Smithy shape ``com.amazonaws.polly#UnsupportedPlsAlphabetException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.error_message


class UnsupportedPlsAlphabetException_(TypedDict, closed=True):
    message: NotRequired["capo_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedPlsAlphabetException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedPlsAlphabetException_:
    out: UnsupportedPlsAlphabetException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedPlsAlphabetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#UnsupportedPlsAlphabetException``."""

    code: str | None = "UnsupportedPlsAlphabetException"

    def __init__(self, data: UnsupportedPlsAlphabetException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedPlsAlphabetException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedPlsAlphabetException":
        return cls(deserialize_json(data))
