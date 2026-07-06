"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ManagedLoginBrandingExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class ManagedLoginBrandingExistsException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedLoginBrandingExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedLoginBrandingExistsException_:
    out: ManagedLoginBrandingExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ManagedLoginBrandingExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#ManagedLoginBrandingExistsException``."""

    code: str | None = "ManagedLoginBrandingExistsException"

    def __init__(self, data: ManagedLoginBrandingExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ManagedLoginBrandingExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ManagedLoginBrandingExistsException":
        return cls(deserialize_aws_json_1_1(data))
