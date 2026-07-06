"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ResourceInUse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.error_message


class ResourceInUse_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInUse_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceInUse_:
    out: ResourceInUse_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceInUse(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#ResourceInUse``."""

    code: str | None = "ResourceInUse"

    def __init__(self, data: ResourceInUse_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUse",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceInUse":
        return cls(deserialize_aws_json_1_1(data))
