"""Generated from Smithy shape ``com.amazonaws.mediapackage#UnprocessableEntityException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackage.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class UnprocessableEntityException_(TypedDict):
    message: NotRequired["aws_sdk_mediapackage.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableEntityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnprocessableEntityException_:
    out: UnprocessableEntityException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnprocessableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediapackage#UnprocessableEntityException``."""

    code: str | None = "UnprocessableEntityException"

    def __init__(self, data: UnprocessableEntityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnprocessableEntityException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnprocessableEntityException":
        return cls(deserialize_json(data))
