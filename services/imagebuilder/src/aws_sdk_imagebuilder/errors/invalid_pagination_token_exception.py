"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InvalidPaginationTokenException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.error_message


class InvalidPaginationTokenException_(TypedDict):
    message: NotRequired["aws_sdk_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidPaginationTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidPaginationTokenException_:
    out: InvalidPaginationTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidPaginationTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#InvalidPaginationTokenException``."""

    code: str | None = "InvalidPaginationTokenException"

    def __init__(self, data: InvalidPaginationTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationTokenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidPaginationTokenException":
        return cls(deserialize_json(data))
