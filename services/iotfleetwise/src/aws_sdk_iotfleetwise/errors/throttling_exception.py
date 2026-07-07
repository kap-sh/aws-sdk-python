"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.retry_after_seconds
    import aws_sdk_iotfleetwise.types.string


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_iotfleetwise.types.string.string"
    quota_code: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>The quota identifier of the applied throttling rules for this request.</p>"""
    service_code: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>The code for the service that couldn't be completed due to throttling.</p>"""
    retry_after_seconds: (
        "aws_sdk_iotfleetwise.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>The number of seconds to wait before retrying the command.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data))
