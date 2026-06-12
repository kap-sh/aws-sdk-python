"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResourceInUseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53resolver.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.string


class ResourceInUseException_(TypedDict):
    message: NotRequired["aws_sdk_route53resolver.types.string.String"]
    resource_type: NotRequired["aws_sdk_route53resolver.types.string.String"]
    """<p>For a <code>ResourceInUseException</code> error, the type of resource that is currently in use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53resolver#ResourceInUseException``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "ResourceInUseException":
        return cls(deserialize_aws_json_1_1(data))
