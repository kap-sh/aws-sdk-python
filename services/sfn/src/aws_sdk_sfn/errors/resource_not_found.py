"""Generated from Smithy shape ``com.amazonaws.sfn#ResourceNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.error_message


class ResourceNotFound_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]
    resource_name: NotRequired["aws_sdk_sfn.types.arn.Arn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFound_:
    out: ResourceNotFound_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out


class ResourceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#ResourceNotFound``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ResourceNotFound":
        return cls(deserialize_aws_json_1_0(data))
