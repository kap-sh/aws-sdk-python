"""Generated from Smithy shape ``com.amazonaws.workspaces#UnsupportedWorkspaceConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.exception_message


class UnsupportedWorkspaceConfigurationException_(TypedDict):
    message: NotRequired["aws_sdk_workspaces.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedWorkspaceConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedWorkspaceConfigurationException_:
    out: UnsupportedWorkspaceConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedWorkspaceConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#UnsupportedWorkspaceConfigurationException``."""

    code: str | None = "UnsupportedWorkspaceConfigurationException"

    def __init__(self, data: UnsupportedWorkspaceConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedWorkspaceConfigurationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "UnsupportedWorkspaceConfigurationException":
        return cls(deserialize_aws_json_1_1(data))
