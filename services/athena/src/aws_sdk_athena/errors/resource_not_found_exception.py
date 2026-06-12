"""Generated from Smithy shape ``com.amazonaws.athena#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_athena.types.amazon_resource_name
    import aws_sdk_athena.types.error_message


class ResourceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_athena.types.error_message.ErrorMessage"]
    resource_name: NotRequired[
        "aws_sdk_athena.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The name of the Amazon resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.athena#ResourceNotFoundException``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
