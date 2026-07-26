"""Generated from Smithy shape ``com.amazonaws.transfer#ResourceExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_transfer.types.message
    import capo_transfer.types.resource
    import capo_transfer.types.resource_type


class ResourceExistsException_(TypedDict, closed=True):
    message: "capo_transfer.types.message.Message"
    resource: "capo_transfer.types.resource.Resource"
    resource_type: "capo_transfer.types.resource_type.ResourceType"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceExistsException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["Resource"] = value["resource"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceExistsException_:
    out: ResourceExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceExistsException_.message required")
    if "Resource" in data:
        out["resource"] = data["Resource"]
    else:
        raise DeserializationError("ResourceExistsException_.resource required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceExistsException_.resource_type required")
    return out


class ResourceExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transfer#ResourceExistsException``."""

    code: str | None = "ResourceExistsException"

    def __init__(self, data: ResourceExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceExistsException":
        return cls(deserialize_aws_json_1_1(data))
