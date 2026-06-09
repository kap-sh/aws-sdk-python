"""Generated from Smithy shape ``com.amazonaws.lambda#SerializedRequestEntityTooLargeException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class SerializedRequestEntityTooLargeException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The error type.</p>"""
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SerializedRequestEntityTooLargeException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SerializedRequestEntityTooLargeException_:
    out: SerializedRequestEntityTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SerializedRequestEntityTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#SerializedRequestEntityTooLargeException``."""

    code: str | None = "SerializedRequestEntityTooLargeException"

    def __init__(self, data: SerializedRequestEntityTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SerializedRequestEntityTooLargeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SerializedRequestEntityTooLargeException":
        return cls(deserialize_json(data))
