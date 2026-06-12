"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CodeDeliveryFailureException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class CodeDeliveryFailureException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message sent when a verification code fails to deliver successfully.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeDeliveryFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeDeliveryFailureException_:
    out: CodeDeliveryFailureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CodeDeliveryFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#CodeDeliveryFailureException``."""

    code: str | None = "CodeDeliveryFailureException"

    def __init__(self, data: CodeDeliveryFailureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CodeDeliveryFailureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CodeDeliveryFailureException":
        return cls(deserialize_aws_json_1_1(data))
