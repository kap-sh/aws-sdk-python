"""Generated from Smithy shape ``com.amazonaws.lambda#KMSDisabledException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class KMSDisabledException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: KMSDisabledException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KMSDisabledException_:
    out: KMSDisabledException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class KMSDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#KMSDisabledException``."""

    code: str | None = "KMSDisabledException"

    def __init__(self, data: KMSDisabledException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSDisabledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KMSDisabledException":
        return cls(deserialize_json(data))
