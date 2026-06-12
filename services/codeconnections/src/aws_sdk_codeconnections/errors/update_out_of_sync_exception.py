"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateOutOfSyncException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeconnections.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.error_message


class UpdateOutOfSyncException_(TypedDict):
    message: NotRequired["aws_sdk_codeconnections.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOutOfSyncException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOutOfSyncException_:
    out: UpdateOutOfSyncException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UpdateOutOfSyncException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeconnections#UpdateOutOfSyncException``."""

    code: str | None = "UpdateOutOfSyncException"

    def __init__(self, data: UpdateOutOfSyncException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UpdateOutOfSyncException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "UpdateOutOfSyncException":
        return cls(deserialize_aws_json_1_0(data))
