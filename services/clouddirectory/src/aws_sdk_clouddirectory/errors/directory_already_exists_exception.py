"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DirectoryAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class DirectoryAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DirectoryAlreadyExistsException_:
    out: DirectoryAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DirectoryAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#DirectoryAlreadyExistsException``."""

    code: str | None = "DirectoryAlreadyExistsException"

    def __init__(self, data: DirectoryAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DirectoryAlreadyExistsException":
        return cls(deserialize_json(data))
