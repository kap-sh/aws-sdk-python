"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PreconditionNotMetException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class PreconditionNotMetException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when a precondition is not met.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreconditionNotMetException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreconditionNotMetException_:
    out: PreconditionNotMetException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PreconditionNotMetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#PreconditionNotMetException``."""

    code: str | None = "PreconditionNotMetException"

    def __init__(self, data: PreconditionNotMetException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreconditionNotMetException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PreconditionNotMetException":
        return cls(deserialize_aws_json_1_1(data))
