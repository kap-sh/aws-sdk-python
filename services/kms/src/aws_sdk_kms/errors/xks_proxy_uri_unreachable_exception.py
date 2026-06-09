"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyUriUnreachableException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class XksProxyUriUnreachableException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XksProxyUriUnreachableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XksProxyUriUnreachableException_:
    out: XksProxyUriUnreachableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class XksProxyUriUnreachableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyUriUnreachableException``."""

    code: str | None = "XksProxyUriUnreachableException"

    def __init__(self, data: XksProxyUriUnreachableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyUriUnreachableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "XksProxyUriUnreachableException":
        return cls(deserialize_aws_json_1_1(data))
