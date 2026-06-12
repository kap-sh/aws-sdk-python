"""Generated from Smithy shape ``com.amazonaws.connect#ResourceInUseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.message
    import aws_sdk_connect.types.resource_type


class ResourceInUseException_(TypedDict):
    message: NotRequired["aws_sdk_connect.types.message.Message"]
    resource_type: NotRequired["aws_sdk_connect.types.resource_type.ResourceType"]
    """<p>The type of resource.</p>"""
    resource_id: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The identifier for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        import aws_sdk_connect.types.resource_type

        out["ResourceType"] = aws_sdk_connect.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        import aws_sdk_connect.types.resource_type

        out["resource_type"] = aws_sdk_connect.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(self, data: ResourceInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceInUseException":
        return cls(deserialize_json(data))
