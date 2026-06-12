"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidSmsRoleTrustRelationshipException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class InvalidSmsRoleTrustRelationshipException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the role trust relationship for the SMS message is not valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidSmsRoleTrustRelationshipException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidSmsRoleTrustRelationshipException_:
    out: InvalidSmsRoleTrustRelationshipException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidSmsRoleTrustRelationshipException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidSmsRoleTrustRelationshipException``."""

    code: str | None = "InvalidSmsRoleTrustRelationshipException"

    def __init__(self, data: InvalidSmsRoleTrustRelationshipException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSmsRoleTrustRelationshipException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InvalidSmsRoleTrustRelationshipException":
        return cls(deserialize_aws_json_1_1(data))
