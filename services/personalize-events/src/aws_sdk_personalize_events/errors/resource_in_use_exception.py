"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ResourceInUseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_personalize_events.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.error_message


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_personalize_events.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.personalizeevents#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(self, data: ResourceInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceInUseException":
        return cls(deserialize_json(data))
