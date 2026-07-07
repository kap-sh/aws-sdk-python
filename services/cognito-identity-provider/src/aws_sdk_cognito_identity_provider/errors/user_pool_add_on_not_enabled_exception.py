"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolAddOnNotEnabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class UserPoolAddOnNotEnabledException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolAddOnNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolAddOnNotEnabledException_:
    out: UserPoolAddOnNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UserPoolAddOnNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolAddOnNotEnabledException``."""

    code: str | None = "UserPoolAddOnNotEnabledException"

    def __init__(self, data: UserPoolAddOnNotEnabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserPoolAddOnNotEnabledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UserPoolAddOnNotEnabledException":
        return cls(deserialize_aws_json_1_1(data))
