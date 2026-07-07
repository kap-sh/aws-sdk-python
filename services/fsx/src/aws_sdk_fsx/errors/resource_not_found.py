"""Generated from Smithy shape ``com.amazonaws.fsx#ResourceNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message
    import aws_sdk_fsx.types.resource_arn


class ResourceNotFound_(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    """<p>The resource ARN of the resource that can't be found.</p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFound_) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFound_:
    out: ResourceNotFound_ = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#ResourceNotFound``."""

    code: str | None = "ResourceNotFound"

    def __init__(self, data: ResourceNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNotFound":
        return cls(deserialize_aws_json_1_1(data))
