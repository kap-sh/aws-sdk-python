"""Generated from Smithy shape ``com.amazonaws.mediapackage#ForbiddenException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackage.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class ForbiddenException_(TypedDict):
    message: NotRequired["aws_sdk_mediapackage.types.__string.__string"]


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
    """Modeled error for Smithy shape ``com.amazonaws.mediapackage#ForbiddenException``."""

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
