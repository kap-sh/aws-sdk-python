"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InvalidRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.string


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_managedblockchain.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchain#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_json(data))
