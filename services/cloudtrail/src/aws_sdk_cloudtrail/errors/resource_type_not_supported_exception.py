"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ResourceTypeNotSupportedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class ResourceTypeNotSupportedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypeNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTypeNotSupportedException_:
    out: ResourceTypeNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceTypeNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#ResourceTypeNotSupportedException``."""

    code: str | None = "ResourceTypeNotSupportedException"

    def __init__(self, data: ResourceTypeNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceTypeNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceTypeNotSupportedException":
        return cls(deserialize_aws_json_1_1(data))
