"""Generated from Smithy shape ``com.amazonaws.mq#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mq.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class ConflictException_(TypedDict, closed=True):
    error_attribute: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The attribute which caused the error.</p>"""
    message: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The explanation of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "error_attribute" in value:
        out["errorAttribute"] = value["error_attribute"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "errorAttribute" in data:
        out["error_attribute"] = data["errorAttribute"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mq#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
