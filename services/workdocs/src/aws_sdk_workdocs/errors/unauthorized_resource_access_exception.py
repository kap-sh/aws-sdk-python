"""Generated from Smithy shape ``com.amazonaws.workdocs#UnauthorizedResourceAccessException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class UnauthorizedResourceAccessException_(TypedDict):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedResourceAccessException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedResourceAccessException_:
    out: UnauthorizedResourceAccessException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnauthorizedResourceAccessException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#UnauthorizedResourceAccessException``."""

    code: str | None = "UnauthorizedResourceAccessException"

    def __init__(self, data: UnauthorizedResourceAccessException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedResourceAccessException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnauthorizedResourceAccessException":
        return cls(deserialize_json(data))
