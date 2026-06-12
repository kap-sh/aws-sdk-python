"""Generated from Smithy shape ``com.amazonaws.batch#ServerException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_batch.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class ServerException_(TypedDict):
    message: NotRequired["aws_sdk_batch.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServerException_:
    out: ServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.batch#ServerException``."""

    code: str | None = "ServerException"

    def __init__(self, data: ServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServerException":
        return cls(deserialize_json(data))
