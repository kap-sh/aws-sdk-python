"""Generated from Smithy shape ``com.amazonaws.lambda#InvalidZipFileException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class InvalidZipFileException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidZipFileException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidZipFileException_:
    out: InvalidZipFileException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidZipFileException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#InvalidZipFileException``."""

    code: str | None = "InvalidZipFileException"

    def __init__(self, data: InvalidZipFileException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidZipFileException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidZipFileException":
        return cls(deserialize_json(data))
