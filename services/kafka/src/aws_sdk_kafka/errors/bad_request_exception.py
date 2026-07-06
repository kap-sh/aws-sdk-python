"""Generated from Smithy shape ``com.amazonaws.kafka#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kafka.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class BadRequestException_(TypedDict, closed=True):
    invalid_parameter: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The parameter that caused the error.</p>"""
    message: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "invalid_parameter" in value:
        out["invalidParameter"] = value["invalid_parameter"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "invalidParameter" in data:
        out["invalid_parameter"] = data["invalidParameter"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kafka#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_json(data))
