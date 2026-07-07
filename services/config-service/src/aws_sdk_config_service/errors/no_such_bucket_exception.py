"""Generated from Smithy shape ``com.amazonaws.configservice#NoSuchBucketException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class NoSuchBucketException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchBucketException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoSuchBucketException_:
    out: NoSuchBucketException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoSuchBucketException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoSuchBucketException``."""

    code: str | None = "NoSuchBucketException"

    def __init__(self, data: NoSuchBucketException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchBucketException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NoSuchBucketException":
        return cls(deserialize_aws_json_1_1(data))
