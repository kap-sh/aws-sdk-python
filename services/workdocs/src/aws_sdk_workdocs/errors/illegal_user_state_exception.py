"""Generated from Smithy shape ``com.amazonaws.workdocs#IllegalUserStateException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class IllegalUserStateException_(TypedDict):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: IllegalUserStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IllegalUserStateException_:
    out: IllegalUserStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IllegalUserStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#IllegalUserStateException``."""

    code: str | None = "IllegalUserStateException"

    def __init__(self, data: IllegalUserStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalUserStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "IllegalUserStateException":
        return cls(deserialize_json(data))
