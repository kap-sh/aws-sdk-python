"""Generated from Smithy shape ``com.amazonaws.s3outposts#OutpostOfflineException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3outposts.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.error_message


class OutpostOfflineException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_s3outposts.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: OutpostOfflineException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> OutpostOfflineException_:
    out: OutpostOfflineException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class OutpostOfflineException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3outposts#OutpostOfflineException``."""

    code: str | None = "OutpostOfflineException"

    def __init__(self, data: OutpostOfflineException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OutpostOfflineException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "OutpostOfflineException":
        return cls(deserialize_json(data))
