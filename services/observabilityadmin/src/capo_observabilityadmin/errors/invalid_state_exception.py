"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#InvalidStateException``."""

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import ServiceError


class InvalidStateException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.observabilityadmin#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(self, data: InvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidStateException":
        return cls(deserialize_json(data))
