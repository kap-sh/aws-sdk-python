"""Generated from Smithy shape ``com.amazonaws.mgn#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.large_bounded_string


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    service_code: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Reached throttling quota exception service code.</p>"""
    quota_code: NotRequired["aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Reached throttling quota exception.</p>"""
    retry_after_seconds: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Reached throttling quota exception will retry after x seconds.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.mgn#ThrottlingException``."""

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
