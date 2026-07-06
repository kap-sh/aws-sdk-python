"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceAlreadyCheckedOutException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class ResourceAlreadyCheckedOutException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAlreadyCheckedOutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceAlreadyCheckedOutException_:
    out: ResourceAlreadyCheckedOutException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceAlreadyCheckedOutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#ResourceAlreadyCheckedOutException``."""

    code: str | None = "ResourceAlreadyCheckedOutException"

    def __init__(self, data: ResourceAlreadyCheckedOutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyCheckedOutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceAlreadyCheckedOutException":
        return cls(deserialize_json(data))
