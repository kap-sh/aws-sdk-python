"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidPasswordException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class InvalidPasswordException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when Amazon Cognito throws an invalid user password exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPasswordException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPasswordException_:
    out: InvalidPasswordException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidPasswordException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidPasswordException``."""

    code: str | None = "InvalidPasswordException"

    def __init__(self, data: InvalidPasswordException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPasswordException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPasswordException":
        return cls(deserialize_aws_json_1_1(data))
