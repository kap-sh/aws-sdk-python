"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ThrottlingException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguru_security.errors import DeserializationError, ServiceError


class ThrottlingException_(TypedDict):
    error_code: "str"
    """<p>The identifier for the error.</p>"""
    message: "str"
    """<p>Description of the error.</p>"""
    service_code: NotRequired["str"]
    """<p>The identifier for the originating service.</p>"""
    quota_code: NotRequired["str"]
    """<p>The identifier for the originating quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["message"] = value["message"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ThrottlingException_.error_code required")
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
    """Modeled error for Smithy shape ``com.amazonaws.codegurusecurity#ThrottlingException``."""

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
