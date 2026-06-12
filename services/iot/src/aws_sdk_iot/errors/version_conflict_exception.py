"""Generated from Smithy shape ``com.amazonaws.iot#VersionConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class VersionConflictException_(TypedDict):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> VersionConflictException_:
    out: VersionConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class VersionConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#VersionConflictException``."""

    code: str | None = "VersionConflictException"

    def __init__(self, data: VersionConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="VersionConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "VersionConflictException":
        return cls(deserialize_json(data))
