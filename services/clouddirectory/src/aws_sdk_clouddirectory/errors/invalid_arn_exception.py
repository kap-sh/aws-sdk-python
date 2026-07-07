"""Generated from Smithy shape ``com.amazonaws.clouddirectory#InvalidArnException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class InvalidArnException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidArnException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidArnException_:
    out: InvalidArnException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidArnException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#InvalidArnException``."""

    code: str | None = "InvalidArnException"

    def __init__(self, data: InvalidArnException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArnException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidArnException":
        return cls(deserialize_json(data))
