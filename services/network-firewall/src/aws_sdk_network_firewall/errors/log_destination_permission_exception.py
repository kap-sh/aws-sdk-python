"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogDestinationPermissionException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.error_message


class LogDestinationPermissionException_(TypedDict):
    message: NotRequired["aws_sdk_network_firewall.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogDestinationPermissionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LogDestinationPermissionException_:
    out: LogDestinationPermissionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class LogDestinationPermissionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkfirewall#LogDestinationPermissionException``."""

    code: str | None = "LogDestinationPermissionException"

    def __init__(self, data: LogDestinationPermissionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LogDestinationPermissionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "LogDestinationPermissionException":
        return cls(deserialize_aws_json_1_0(data))
