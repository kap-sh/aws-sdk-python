"""Generated from Smithy shape ``com.amazonaws.lambda#KMSNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class KMSNotFoundException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: KMSNotFoundException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KMSNotFoundException_:
    out: KMSNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class KMSNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#KMSNotFoundException``."""

    code: str | None = "KMSNotFoundException"

    def __init__(self, data: KMSNotFoundException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KMSNotFoundException":
        return cls(deserialize_json(data))
