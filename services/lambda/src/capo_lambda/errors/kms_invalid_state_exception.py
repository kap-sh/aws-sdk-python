"""Generated from Smithy shape ``com.amazonaws.lambda#KMSInvalidStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class KMSInvalidStateException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: KMSInvalidStateException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KMSInvalidStateException_:
    out: KMSInvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class KMSInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#KMSInvalidStateException``."""

    code: str | None = "KMSInvalidStateException"

    def __init__(self, data: KMSInvalidStateException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInvalidStateException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "KMSInvalidStateException":
        return cls(deserialize_json(data), message)
