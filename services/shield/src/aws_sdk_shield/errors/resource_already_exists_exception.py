"""Generated from Smithy shape ``com.amazonaws.shield#ResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_shield.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_shield.types.error_message
    import aws_sdk_shield.types.string


class ResourceAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_shield.types.error_message.errorMessage"]
    resource_type: NotRequired["aws_sdk_shield.types.string.String"]
    """<p>The type of resource that already exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAlreadyExistsException_:
    out: ResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#ResourceAlreadyExistsException``."""

    code: str | None = "ResourceAlreadyExistsException"

    def __init__(self, data: ResourceAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
