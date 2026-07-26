"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserLambdaValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class UserLambdaValidationException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the Amazon Cognito service returns a user validation exception with the Lambda service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserLambdaValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserLambdaValidationException_:
    out: UserLambdaValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UserLambdaValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UserLambdaValidationException``."""

    code: str | None = "UserLambdaValidationException"

    def __init__(self, data: UserLambdaValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserLambdaValidationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UserLambdaValidationException":
        return cls(deserialize_aws_json_1_1(data))
