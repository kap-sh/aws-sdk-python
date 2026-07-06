"""Generated from Smithy shape ``com.amazonaws.iot#DeleteConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class DeleteConflictException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteConflictException_:
    out: DeleteConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DeleteConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#DeleteConflictException``."""

    code: str | None = "DeleteConflictException"

    def __init__(self, data: DeleteConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeleteConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeleteConflictException":
        return cls(deserialize_json(data))
