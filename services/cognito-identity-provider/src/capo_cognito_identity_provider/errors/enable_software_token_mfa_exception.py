"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EnableSoftwareTokenMFAException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class EnableSoftwareTokenMFAException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableSoftwareTokenMFAException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableSoftwareTokenMFAException_:
    out: EnableSoftwareTokenMFAException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class EnableSoftwareTokenMFAException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#EnableSoftwareTokenMFAException``."""

    code: str | None = "EnableSoftwareTokenMFAException"

    def __init__(self, data: EnableSoftwareTokenMFAException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EnableSoftwareTokenMFAException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EnableSoftwareTokenMFAException":
        return cls(deserialize_aws_json_1_1(data))
