"""Generated from Smithy shape ``com.amazonaws.artifact#InternalServerException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_artifact.errors import DeserializationError, ServiceError


class InternalServerException_(TypedDict, closed=True):
    message: "str"
    retry_after_seconds: NotRequired["int"]
    """<p>Number of seconds in which the caller can retry the request.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.artifact#InternalServerException``."""

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
