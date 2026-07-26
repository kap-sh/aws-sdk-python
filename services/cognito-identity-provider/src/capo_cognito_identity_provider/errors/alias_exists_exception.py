"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AliasExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class AliasExistsException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message that Amazon Cognito sends to the user when the value of an alias attribute is already linked to another user profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AliasExistsException_:
    out: AliasExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AliasExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#AliasExistsException``."""

    code: str | None = "AliasExistsException"

    def __init__(self, data: AliasExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AliasExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AliasExistsException":
        return cls(deserialize_aws_json_1_1(data))
