"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#MFAMethodNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class MFAMethodNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when Amazon Cognito throws an MFA method not found exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MFAMethodNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MFAMethodNotFoundException_:
    out: MFAMethodNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MFAMethodNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#MFAMethodNotFoundException``."""

    code: str | None = "MFAMethodNotFoundException"

    def __init__(self, data: MFAMethodNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MFAMethodNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MFAMethodNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
