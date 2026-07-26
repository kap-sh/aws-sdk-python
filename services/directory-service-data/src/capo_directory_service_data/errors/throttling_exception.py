"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_directory_service_data.types.exception_message


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_directory_service_data.types.exception_message.ExceptionMessage"
    retry_after_seconds: NotRequired["int"]
    """<p> The recommended amount of seconds to retry after a throttling exception. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservicedata#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
