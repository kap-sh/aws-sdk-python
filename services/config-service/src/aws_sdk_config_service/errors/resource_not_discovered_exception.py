"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceNotDiscoveredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class ResourceNotDiscoveredException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotDiscoveredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotDiscoveredException_:
    out: ResourceNotDiscoveredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceNotDiscoveredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#ResourceNotDiscoveredException``."""

    code: str | None = "ResourceNotDiscoveredException"

    def __init__(self, data: ResourceNotDiscoveredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotDiscoveredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNotDiscoveredException":
        return cls(deserialize_aws_json_1_1(data))
