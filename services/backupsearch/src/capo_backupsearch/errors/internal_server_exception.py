"""Generated from Smithy shape ``com.amazonaws.backupsearch#InternalServerException``."""

from typing_extensions import NotRequired, TypedDict

from capo_backupsearch.errors import DeserializationError, ServiceError


class InternalServerException_(TypedDict, closed=True):
    message: "str"
    """<p>Unexpected error during processing of request.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>Retry the call after number of seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backupsearch#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))
