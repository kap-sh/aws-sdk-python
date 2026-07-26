"""Generated from Smithy shape ``com.amazonaws.networkmanager#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_networkmanager.types.retry_after_seconds
    import capo_networkmanager.types.server_side_string


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_networkmanager.types.server_side_string.ServerSideString"
    retry_after_seconds: NotRequired[
        "capo_networkmanager.types.retry_after_seconds.RetryAfterSeconds"
    ]
    """<p>Indicates when to retry the request.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
