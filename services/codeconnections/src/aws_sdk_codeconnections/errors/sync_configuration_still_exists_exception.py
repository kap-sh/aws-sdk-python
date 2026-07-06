"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncConfigurationStillExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeconnections.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.error_message


class SyncConfigurationStillExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codeconnections.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncConfigurationStillExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncConfigurationStillExistsException_:
    out: SyncConfigurationStillExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SyncConfigurationStillExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeconnections#SyncConfigurationStillExistsException``."""

    code: str | None = "SyncConfigurationStillExistsException"

    def __init__(self, data: SyncConfigurationStillExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SyncConfigurationStillExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "SyncConfigurationStillExistsException":
        return cls(deserialize_aws_json_1_0(data))
