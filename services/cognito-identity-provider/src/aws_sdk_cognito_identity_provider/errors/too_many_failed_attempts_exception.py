"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TooManyFailedAttemptsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class TooManyFailedAttemptsException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when Amazon Cognito returns a <code>TooManyFailedAttempts</code> exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyFailedAttemptsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyFailedAttemptsException_:
    out: TooManyFailedAttemptsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TooManyFailedAttemptsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#TooManyFailedAttemptsException``."""

    code: str | None = "TooManyFailedAttemptsException"

    def __init__(self, data: TooManyFailedAttemptsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyFailedAttemptsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TooManyFailedAttemptsException":
        return cls(deserialize_aws_json_1_1(data))
