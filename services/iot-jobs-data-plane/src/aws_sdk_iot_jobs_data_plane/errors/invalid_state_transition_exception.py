"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#InvalidStateTransitionException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_jobs_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.error_message


class InvalidStateTransitionException_(TypedDict):
    message: NotRequired["aws_sdk_iot_jobs_data_plane.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidStateTransitionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidStateTransitionException_:
    out: InvalidStateTransitionException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidStateTransitionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotjobsdataplane#InvalidStateTransitionException``."""

    code: str | None = "InvalidStateTransitionException"

    def __init__(self, data: InvalidStateTransitionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateTransitionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidStateTransitionException":
        return cls(deserialize_json(data))
