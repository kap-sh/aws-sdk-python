"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaTimeoutException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kafka.errors import ServiceError

if TYPE_CHECKING:
    import capo_kafka.types.__string


class KafkaTimeoutException_(TypedDict, closed=True):
    invalid_parameter: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The parameter that caused the error.</p>"""
    message: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaTimeoutException_) -> dict:
    out: dict = {}
    if "invalid_parameter" in value:
        out["invalidParameter"] = value["invalid_parameter"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KafkaTimeoutException_:
    out: KafkaTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "invalidParameter" in data:
        out["invalid_parameter"] = data["invalidParameter"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KafkaTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kafka#KafkaTimeoutException``."""

    code: str | None = "KafkaTimeoutException"

    def __init__(self, data: KafkaTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KafkaTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KafkaTimeoutException":
        return cls(deserialize_json(data))
