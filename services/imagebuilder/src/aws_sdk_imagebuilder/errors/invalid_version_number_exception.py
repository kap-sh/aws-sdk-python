"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InvalidVersionNumberException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.error_message


class InvalidVersionNumberException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidVersionNumberException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidVersionNumberException_:
    out: InvalidVersionNumberException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidVersionNumberException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#InvalidVersionNumberException``."""

    code: str | None = "InvalidVersionNumberException"

    def __init__(self, data: InvalidVersionNumberException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidVersionNumberException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidVersionNumberException":
        return cls(deserialize_json(data))
