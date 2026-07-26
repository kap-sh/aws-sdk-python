"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnNotEnabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class WebAuthnNotEnabledException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebAuthnNotEnabledException_:
    out: WebAuthnNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WebAuthnNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnNotEnabledException``."""

    code: str | None = "WebAuthnNotEnabledException"

    def __init__(self, data: WebAuthnNotEnabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WebAuthnNotEnabledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WebAuthnNotEnabledException":
        return cls(deserialize_aws_json_1_1(data))
