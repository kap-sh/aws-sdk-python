"""Generated from Smithy shape ``com.amazonaws.workdocs#ProhibitedStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class ProhibitedStateException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: ProhibitedStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ProhibitedStateException_:
    out: ProhibitedStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ProhibitedStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#ProhibitedStateException``."""

    code: str | None = "ProhibitedStateException"

    def __init__(self, data: ProhibitedStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ProhibitedStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ProhibitedStateException":
        return cls(deserialize_json(data))
