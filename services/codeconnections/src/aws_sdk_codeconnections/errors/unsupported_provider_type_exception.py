"""Generated from Smithy shape ``com.amazonaws.codeconnections#UnsupportedProviderTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeconnections.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.error_message


class UnsupportedProviderTypeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codeconnections.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnsupportedProviderTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnsupportedProviderTypeException_:
    out: UnsupportedProviderTypeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedProviderTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeconnections#UnsupportedProviderTypeException``."""

    code: str | None = "UnsupportedProviderTypeException"

    def __init__(self, data: UnsupportedProviderTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedProviderTypeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "UnsupportedProviderTypeException":
        return cls(deserialize_aws_json_1_0(data))
