"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#TerminalStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_jobs_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.error_message


class TerminalStateException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iot_jobs_data_plane.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: TerminalStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TerminalStateException_:
    out: TerminalStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TerminalStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotjobsdataplane#TerminalStateException``."""

    code: str | None = "TerminalStateException"

    def __init__(self, data: TerminalStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TerminalStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TerminalStateException":
        return cls(deserialize_json(data))
