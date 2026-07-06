"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RefreshTokenReuseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class RefreshTokenReuseException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshTokenReuseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshTokenReuseException_:
    out: RefreshTokenReuseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RefreshTokenReuseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#RefreshTokenReuseException``."""

    code: str | None = "RefreshTokenReuseException"

    def __init__(self, data: RefreshTokenReuseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RefreshTokenReuseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RefreshTokenReuseException":
        return cls(deserialize_aws_json_1_1(data))
