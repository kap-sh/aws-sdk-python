"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.retry_after_seconds
    import aws_sdk_greengrassv2.types.string


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_greengrassv2.types.string.String"
    quota_code: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    r"""<p>The code for the quota in <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html\">Service Quotas</a>.</p>"""
    service_code: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    r"""<p>The code for the service in <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html\">Service Quotas</a>.</p>"""
    retry_after_seconds: (
        "aws_sdk_greengrassv2.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>The amount of time to wait before you retry the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
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
    """Modeled error for Smithy shape ``com.amazonaws.greengrassv2#ThrottlingException``."""

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
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
