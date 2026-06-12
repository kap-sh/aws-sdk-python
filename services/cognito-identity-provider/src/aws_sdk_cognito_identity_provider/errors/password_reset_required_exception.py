"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordResetRequiredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class PasswordResetRequiredException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when a password reset is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PasswordResetRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PasswordResetRequiredException_:
    out: PasswordResetRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PasswordResetRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordResetRequiredException``."""

    code: str | None = "PasswordResetRequiredException"

    def __init__(self, data: PasswordResetRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PasswordResetRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PasswordResetRequiredException":
        return cls(deserialize_aws_json_1_1(data))
