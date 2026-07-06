"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UnsupportedUserStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class UnsupportedUserStateException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the user is in an unsupported state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedUserStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedUserStateException_:
    out: UnsupportedUserStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedUserStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UnsupportedUserStateException``."""

    code: str | None = "UnsupportedUserStateException"

    def __init__(self, data: UnsupportedUserStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedUserStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedUserStateException":
        return cls(deserialize_aws_json_1_1(data))
