"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordHistoryPolicyViolationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class PasswordHistoryPolicyViolationException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PasswordHistoryPolicyViolationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PasswordHistoryPolicyViolationException_:
    out: PasswordHistoryPolicyViolationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PasswordHistoryPolicyViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordHistoryPolicyViolationException``."""

    code: str | None = "PasswordHistoryPolicyViolationException"

    def __init__(self, data: PasswordHistoryPolicyViolationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PasswordHistoryPolicyViolationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PasswordHistoryPolicyViolationException":
        return cls(deserialize_aws_json_1_1(data))
