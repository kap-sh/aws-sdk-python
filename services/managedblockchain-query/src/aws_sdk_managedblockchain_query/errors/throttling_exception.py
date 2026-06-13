"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.exception_message
    import aws_sdk_managedblockchain_query.types.quota_code
    import aws_sdk_managedblockchain_query.types.service_code


class ThrottlingException_(TypedDict):
    message: "aws_sdk_managedblockchain_query.types.exception_message.ExceptionMessage"
    """<p>The container for the exception message.</p>"""
    service_code: "aws_sdk_managedblockchain_query.types.service_code.ServiceCode"
    """<p>The container for the <code>serviceCode</code>.</p>"""
    quota_code: "aws_sdk_managedblockchain_query.types.quota_code.QuotaCode"
    """<p>The container for the <code>quotaCode</code>.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The container of the <code>retryAfterSeconds</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["serviceCode"] = value["service_code"]
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
    else:
        raise DeserializationError("ThrottlingException_.service_code required")
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    else:
        raise DeserializationError("ThrottlingException_.quota_code required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchainquery#ThrottlingException``."""

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
