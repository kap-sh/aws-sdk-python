"""Generated from Smithy shape ``com.amazonaws.iot#TaskAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class TaskAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TaskAlreadyExistsException_:
    out: TaskAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TaskAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#TaskAlreadyExistsException``."""

    code: str | None = "TaskAlreadyExistsException"

    def __init__(self, data: TaskAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TaskAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TaskAlreadyExistsException":
        return cls(deserialize_json(data))
