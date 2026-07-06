"""Generated from Smithy shape ``com.amazonaws.licensemanager#ServerInternalException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.message


class ServerInternalException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerInternalException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerInternalException_:
    out: ServerInternalException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ServerInternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#ServerInternalException``."""

    code: str | None = "ServerInternalException"

    def __init__(self, data: ServerInternalException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerInternalException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServerInternalException":
        return cls(deserialize_aws_json_1_1(data))
