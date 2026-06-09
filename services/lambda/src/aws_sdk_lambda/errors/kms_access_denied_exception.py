"""Generated from Smithy shape ``com.amazonaws.lambda#KMSAccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class KMSAccessDeniedException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: KMSAccessDeniedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KMSAccessDeniedException_:
    out: KMSAccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class KMSAccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#KMSAccessDeniedException``."""

    code: str | None = "KMSAccessDeniedException"

    def __init__(self, data: KMSAccessDeniedException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSAccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KMSAccessDeniedException":
        return cls(deserialize_json(data))
