"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ForbiddenException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.error_message


class ForbiddenException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(self, data: ForbiddenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ForbiddenException":
        return cls(deserialize_json(data))
