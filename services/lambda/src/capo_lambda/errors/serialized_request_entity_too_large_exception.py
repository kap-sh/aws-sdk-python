"""Generated from Smithy shape ``com.amazonaws.lambda#SerializedRequestEntityTooLargeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class SerializedRequestEntityTooLargeException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>The error type.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]


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
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class SerializedRequestEntityTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#SerializedRequestEntityTooLargeException``."""

    code: str | None = "SerializedRequestEntityTooLargeException"

    def __init__(
        self,
        data: SerializedRequestEntityTooLargeException_,
        message: str | None = None,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SerializedRequestEntityTooLargeException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "SerializedRequestEntityTooLargeException":
        return cls(deserialize_json(data), message)
