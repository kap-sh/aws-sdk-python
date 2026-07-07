"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UnsupportedTokenTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class UnsupportedTokenTypeException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedTokenTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedTokenTypeException_:
    out: UnsupportedTokenTypeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedTokenTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UnsupportedTokenTypeException``."""

    code: str | None = "UnsupportedTokenTypeException"

    def __init__(self, data: UnsupportedTokenTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedTokenTypeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedTokenTypeException":
        return cls(deserialize_aws_json_1_1(data))
