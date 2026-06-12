"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnOriginNotAllowedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class WebAuthnOriginNotAllowedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnOriginNotAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebAuthnOriginNotAllowedException_:
    out: WebAuthnOriginNotAllowedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WebAuthnOriginNotAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnOriginNotAllowedException``."""

    code: str | None = "WebAuthnOriginNotAllowedException"

    def __init__(self, data: WebAuthnOriginNotAllowedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WebAuthnOriginNotAllowedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WebAuthnOriginNotAllowedException":
        return cls(deserialize_aws_json_1_1(data))
