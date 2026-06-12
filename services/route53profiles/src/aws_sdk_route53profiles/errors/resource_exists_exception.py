"""Generated from Smithy shape ``com.amazonaws.route53profiles#ResourceExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53profiles.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.string


class ResourceExistsException_(TypedDict):
    message: NotRequired["aws_sdk_route53profiles.types.string.String"]
    resource_type: NotRequired["aws_sdk_route53profiles.types.string.String"]
    """<p> The resource type that caused the resource exists exception. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceExistsException_:
    out: ResourceExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53profiles#ResourceExistsException``."""

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
    def from_json(cls, data: dict) -> "ResourceExistsException":
        return cls(deserialize_json(data))
