"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_notificationscontacts.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.error_message
    import aws_sdk_notificationscontacts.types.quota_code
    import aws_sdk_notificationscontacts.types.service_code


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_notificationscontacts.types.error_message.ErrorMessage"
    service_code: NotRequired[
        "aws_sdk_notificationscontacts.types.service_code.ServiceCode"
    ]
    """<p>Identifies the service being throttled.</p>"""
    quota_code: NotRequired["aws_sdk_notificationscontacts.types.quota_code.QuotaCode"]
    """<p>Identifies the quota that is being throttled.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds a client should wait before retrying the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.notificationscontacts#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
