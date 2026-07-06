"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ThrottlingException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError, ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    """<p>A message describing the throttling error.</p>"""
    service_code: NotRequired["str"]
    """<p>The service code associated with the throttling error.</p>"""
    quota_code: NotRequired["str"]
    """<p>The quota code associated with the throttling error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
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
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralchannel#ThrottlingException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data))
