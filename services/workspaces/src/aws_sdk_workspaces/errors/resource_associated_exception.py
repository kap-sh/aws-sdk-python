"""Generated from Smithy shape ``com.amazonaws.workspaces#ResourceAssociatedException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.exception_message


class ResourceAssociatedException_(TypedDict):
    message: NotRequired["aws_sdk_workspaces.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAssociatedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAssociatedException_:
    out: ResourceAssociatedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceAssociatedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#ResourceAssociatedException``."""

    code: str | None = "ResourceAssociatedException"

    def __init__(self, data: ResourceAssociatedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAssociatedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceAssociatedException":
        return cls(deserialize_aws_json_1_1(data))
