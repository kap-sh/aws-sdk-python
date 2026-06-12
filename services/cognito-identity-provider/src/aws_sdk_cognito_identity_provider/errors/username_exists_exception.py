"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UsernameExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class UsernameExistsException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when Amazon Cognito throws a user name exists exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsernameExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UsernameExistsException_:
    out: UsernameExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UsernameExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UsernameExistsException``."""

    code: str | None = "UsernameExistsException"

    def __init__(self, data: UsernameExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UsernameExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UsernameExistsException":
        return cls(deserialize_aws_json_1_1(data))
