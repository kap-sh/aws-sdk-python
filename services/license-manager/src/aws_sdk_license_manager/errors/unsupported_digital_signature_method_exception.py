"""Generated from Smithy shape ``com.amazonaws.licensemanager#UnsupportedDigitalSignatureMethodException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.message


class UnsupportedDigitalSignatureMethodException_(TypedDict):
    message: NotRequired["aws_sdk_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedDigitalSignatureMethodException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedDigitalSignatureMethodException_:
    out: UnsupportedDigitalSignatureMethodException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedDigitalSignatureMethodException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#UnsupportedDigitalSignatureMethodException``."""

    code: str | None = "UnsupportedDigitalSignatureMethodException"

    def __init__(self, data: UnsupportedDigitalSignatureMethodException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedDigitalSignatureMethodException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "UnsupportedDigitalSignatureMethodException":
        return cls(deserialize_aws_json_1_1(data))
