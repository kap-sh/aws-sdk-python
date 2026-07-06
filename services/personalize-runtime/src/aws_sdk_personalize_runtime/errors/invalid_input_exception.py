"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#InvalidInputException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_personalize_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.error_message


class InvalidInputException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_personalize_runtime.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidInputException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.personalizeruntime#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(self, data: InvalidInputException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidInputException":
        return cls(deserialize_json(data))
