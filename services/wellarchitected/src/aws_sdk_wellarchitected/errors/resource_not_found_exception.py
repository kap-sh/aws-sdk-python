"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wellarchitected.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.exception_message
    import aws_sdk_wellarchitected.types.exception_resource_id
    import aws_sdk_wellarchitected.types.exception_resource_type


class ResourceNotFoundException_(TypedDict):
    message: NotRequired[
        "aws_sdk_wellarchitected.types.exception_message.ExceptionMessage"
    ]
    resource_id: NotRequired[
        "aws_sdk_wellarchitected.types.exception_resource_id.ExceptionResourceId"
    ]
    resource_type: NotRequired[
        "aws_sdk_wellarchitected.types.exception_resource_type.ExceptionResourceType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wellarchitected#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))
