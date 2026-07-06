"""Generated from Smithy shape ``com.amazonaws.kafka#UnknownTopicOrPartitionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kafka.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class UnknownTopicOrPartitionException_(TypedDict, closed=True):
    invalid_parameter: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The parameter that caused the error.</p>"""
    message: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnknownTopicOrPartitionException_) -> dict:
    out: dict = {}
    if "invalid_parameter" in value:
        out["invalidParameter"] = value["invalid_parameter"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnknownTopicOrPartitionException_:
    out: UnknownTopicOrPartitionException_ = {}  # type: ignore[typeddict-item]
    if "invalidParameter" in data:
        out["invalid_parameter"] = data["invalidParameter"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnknownTopicOrPartitionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kafka#UnknownTopicOrPartitionException``."""

    code: str | None = "UnknownTopicOrPartitionException"

    def __init__(self, data: UnknownTopicOrPartitionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnknownTopicOrPartitionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnknownTopicOrPartitionException":
        return cls(deserialize_json(data))
