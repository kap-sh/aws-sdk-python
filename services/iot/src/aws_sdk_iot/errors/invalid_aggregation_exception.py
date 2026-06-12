"""Generated from Smithy shape ``com.amazonaws.iot#InvalidAggregationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class InvalidAggregationException_(TypedDict):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidAggregationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidAggregationException_:
    out: InvalidAggregationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidAggregationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#InvalidAggregationException``."""

    code: str | None = "InvalidAggregationException"

    def __init__(self, data: InvalidAggregationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAggregationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidAggregationException":
        return cls(deserialize_json(data))
