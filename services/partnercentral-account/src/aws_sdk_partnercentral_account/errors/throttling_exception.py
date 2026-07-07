"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ThrottlingException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError, ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    service_code: NotRequired["str"]
    """<p>The service code associated with the throttling error.</p>"""
    quota_code: NotRequired["str"]
    """<p>The quota code associated with the throttling error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralaccount#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data))
