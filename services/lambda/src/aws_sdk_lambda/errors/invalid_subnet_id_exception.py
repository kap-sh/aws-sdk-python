"""Generated from Smithy shape ``com.amazonaws.lambda#InvalidSubnetIDException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class InvalidSubnetIDException_(TypedDict, closed=True):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidSubnetIDException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidSubnetIDException_:
    out: InvalidSubnetIDException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidSubnetIDException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#InvalidSubnetIDException``."""

    code: str | None = "InvalidSubnetIDException"

    def __init__(self, data: InvalidSubnetIDException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSubnetIDException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidSubnetIDException":
        return cls(deserialize_json(data))
