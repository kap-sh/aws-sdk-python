"""Generated from Smithy shape ``com.amazonaws.kafka#NotControllerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kafka.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class NotControllerException_(TypedDict, closed=True):
    invalid_parameter: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The parameter that caused the error.</p>"""
    message: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotControllerException_) -> dict:
    out: dict = {}
    if "invalid_parameter" in value:
        out["invalidParameter"] = value["invalid_parameter"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotControllerException_:
    out: NotControllerException_ = {}  # type: ignore[typeddict-item]
    if "invalidParameter" in data:
        out["invalid_parameter"] = data["invalidParameter"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NotControllerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kafka#NotControllerException``."""

    code: str | None = "NotControllerException"

    def __init__(self, data: NotControllerException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotControllerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotControllerException":
        return cls(deserialize_json(data))
