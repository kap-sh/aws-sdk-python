"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DirectoryNotEnabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class DirectoryNotEnabledException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DirectoryNotEnabledException_:
    out: DirectoryNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DirectoryNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#DirectoryNotEnabledException``."""

    code: str | None = "DirectoryNotEnabledException"

    def __init__(self, data: DirectoryNotEnabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryNotEnabledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DirectoryNotEnabledException":
        return cls(deserialize_json(data))
