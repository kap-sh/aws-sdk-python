"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectNotDetachedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class ObjectNotDetachedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectNotDetachedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ObjectNotDetachedException_:
    out: ObjectNotDetachedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ObjectNotDetachedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#ObjectNotDetachedException``."""

    code: str | None = "ObjectNotDetachedException"

    def __init__(self, data: ObjectNotDetachedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ObjectNotDetachedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ObjectNotDetachedException":
        return cls(deserialize_json(data))
