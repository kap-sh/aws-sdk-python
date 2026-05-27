"""Generated from Smithy shape ``com.amazonaws.lambda#EFSMountFailureException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class EFSMountFailureException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: EFSMountFailureException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EFSMountFailureException_:
    out: EFSMountFailureException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EFSMountFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#EFSMountFailureException``."""

    code: str | None = "EFSMountFailureException"

    def __init__(self, data: EFSMountFailureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EFSMountFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EFSMountFailureException":
        return cls(deserialize_json(data))
