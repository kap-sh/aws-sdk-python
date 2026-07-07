"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesDefaultRoleNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.exception_message


class WorkspacesDefaultRoleNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workspaces.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesDefaultRoleNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesDefaultRoleNotFoundException_:
    out: WorkspacesDefaultRoleNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WorkspacesDefaultRoleNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#WorkspacesDefaultRoleNotFoundException``."""

    code: str | None = "WorkspacesDefaultRoleNotFoundException"

    def __init__(self, data: WorkspacesDefaultRoleNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WorkspacesDefaultRoleNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WorkspacesDefaultRoleNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
