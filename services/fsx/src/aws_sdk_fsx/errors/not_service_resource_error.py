"""Generated from Smithy shape ``com.amazonaws.fsx#NotServiceResourceError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message
    import aws_sdk_fsx.types.resource_arn


class NotServiceResourceError_(TypedDict):
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the non-Amazon FSx resource.</p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotServiceResourceError_) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotServiceResourceError_:
    out: NotServiceResourceError_ = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NotServiceResourceError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#NotServiceResourceError``."""

    code: str | None = "NotServiceResourceError"

    def __init__(self, data: NotServiceResourceError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotServiceResourceError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NotServiceResourceError":
        return cls(deserialize_aws_json_1_1(data))
