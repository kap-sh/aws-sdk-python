"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidUserPoolConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class InvalidUserPoolConfigurationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the user pool configuration is not valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidUserPoolConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidUserPoolConfigurationException_:
    out: InvalidUserPoolConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidUserPoolConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidUserPoolConfigurationException``."""

    code: str | None = "InvalidUserPoolConfigurationException"

    def __init__(self, data: InvalidUserPoolConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidUserPoolConfigurationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidUserPoolConfigurationException":
        return cls(deserialize_aws_json_1_1(data))
