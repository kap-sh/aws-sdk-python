"""Generated from Smithy shape ``com.amazonaws.lambda#InvalidSecurityGroupIDException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class InvalidSecurityGroupIDException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidSecurityGroupIDException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidSecurityGroupIDException_:
    out: InvalidSecurityGroupIDException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidSecurityGroupIDException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#InvalidSecurityGroupIDException``."""

    code: str | None = "InvalidSecurityGroupIDException"

    def __init__(self, data: InvalidSecurityGroupIDException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSecurityGroupIDException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidSecurityGroupIDException":
        return cls(deserialize_json(data))
