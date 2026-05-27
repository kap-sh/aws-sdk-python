"""Generated from Smithy shape ``com.amazonaws.lambda#EFSIOException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class EFSIOException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: EFSIOException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EFSIOException_:
    out: EFSIOException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EFSIOException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#EFSIOException``."""

    code: str | None = "EFSIOException"

    def __init__(self, data: EFSIOException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EFSIOException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EFSIOException":
        return cls(deserialize_json(data))
