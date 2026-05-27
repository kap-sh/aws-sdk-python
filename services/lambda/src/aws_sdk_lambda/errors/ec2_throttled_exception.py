"""Generated from Smithy shape ``com.amazonaws.lambda#EC2ThrottledException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class EC2ThrottledException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: EC2ThrottledException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EC2ThrottledException_:
    out: EC2ThrottledException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EC2ThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#EC2ThrottledException``."""

    code: str | None = "EC2ThrottledException"

    def __init__(self, data: EC2ThrottledException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="EC2ThrottledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EC2ThrottledException":
        return cls(deserialize_json(data))
