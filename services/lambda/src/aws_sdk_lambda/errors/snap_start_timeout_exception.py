"""Generated from Smithy shape ``com.amazonaws.lambda#SnapStartTimeoutException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class SnapStartTimeoutException_(TypedDict, closed=True):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SnapStartTimeoutException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SnapStartTimeoutException_:
    out: SnapStartTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SnapStartTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#SnapStartTimeoutException``."""

    code: str | None = "SnapStartTimeoutException"

    def __init__(self, data: SnapStartTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapStartTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SnapStartTimeoutException":
        return cls(deserialize_json(data))
