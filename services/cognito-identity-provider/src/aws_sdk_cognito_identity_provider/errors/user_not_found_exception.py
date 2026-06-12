"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class UserNotFoundException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when a user isn't found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserNotFoundException_:
    out: UserNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UserNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UserNotFoundException``."""

    code: str | None = "UserNotFoundException"

    def __init__(self, data: UserNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UserNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
