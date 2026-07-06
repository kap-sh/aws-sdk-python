"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ScopeDoesNotExistException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class ScopeDoesNotExistException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeDoesNotExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScopeDoesNotExistException_:
    out: ScopeDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ScopeDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#ScopeDoesNotExistException``."""

    code: str | None = "ScopeDoesNotExistException"

    def __init__(self, data: ScopeDoesNotExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ScopeDoesNotExistException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ScopeDoesNotExistException":
        return cls(deserialize_aws_json_1_1(data))
