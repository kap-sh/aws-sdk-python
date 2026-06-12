"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#SessionExpiredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_signaling.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_signaling.types.error_message


class SessionExpiredException_(TypedDict):
    message: NotRequired[
        "aws_sdk_kinesis_video_signaling.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SessionExpiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SessionExpiredException_:
    out: SessionExpiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SessionExpiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideosignaling#SessionExpiredException``."""

    code: str | None = "SessionExpiredException"

    def __init__(self, data: SessionExpiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionExpiredException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SessionExpiredException":
        return cls(deserialize_json(data))
