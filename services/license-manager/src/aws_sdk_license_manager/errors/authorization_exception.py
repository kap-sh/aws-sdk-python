"""Generated from Smithy shape ``com.amazonaws.licensemanager#AuthorizationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.message


class AuthorizationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthorizationException_:
    out: AuthorizationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AuthorizationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#AuthorizationException``."""

    code: str | None = "AuthorizationException"

    def __init__(self, data: AuthorizationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AuthorizationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AuthorizationException":
        return cls(deserialize_aws_json_1_1(data))
