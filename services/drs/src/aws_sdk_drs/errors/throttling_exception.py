"""Generated from Smithy shape ``com.amazonaws.drs#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_drs.types.large_bounded_string


class ThrottlingException_(TypedDict):
    message: "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    service_code: NotRequired[
        "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Service code.</p>"""
    quota_code: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Quota code.</p>"""
    retry_after_seconds: NotRequired[
        "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>The number of seconds after which the request should be safe to retry.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.drs#ThrottlingException``."""

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
