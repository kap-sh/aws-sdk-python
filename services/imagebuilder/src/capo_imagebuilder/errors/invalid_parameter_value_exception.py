"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InvalidParameterValueException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import capo_imagebuilder.types.error_message


class InvalidParameterValueException_(TypedDict, closed=True):
    message: NotRequired["capo_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#InvalidParameterValueException``."""

    code: str | None = "InvalidParameterValueException"

    def __init__(self, data: InvalidParameterValueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterValueException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterValueException":
        return cls(deserialize_json(data))
