"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InternalErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class InternalErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when Amazon Cognito throws an internal error exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalErrorException_:
    out: InternalErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#InternalErrorException``."""

    code: str | None = "InternalErrorException"

    def __init__(self, data: InternalErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalErrorException":
        return cls(deserialize_aws_json_1_1(data))
