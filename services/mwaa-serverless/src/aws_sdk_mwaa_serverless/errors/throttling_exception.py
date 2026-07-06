"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mwaa_serverless.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.error_message


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_mwaa_serverless.types.error_message.ErrorMessage"
    service_code: "str"
    """<p>The code for the service.</p>"""
    quota_code: "str"
    """<p>The code of the quota.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ServiceCode"] = value["service_code"]
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
    else:
        raise DeserializationError("ThrottlingException_.service_code required")
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError("ThrottlingException_.quota_code required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mwaaserverless#ThrottlingException``."""

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
