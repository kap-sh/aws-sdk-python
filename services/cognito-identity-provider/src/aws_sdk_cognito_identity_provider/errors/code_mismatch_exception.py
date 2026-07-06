"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CodeMismatchException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class CodeMismatchException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message provided when the code mismatch exception is thrown.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeMismatchException_:
    out: CodeMismatchException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CodeMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#CodeMismatchException``."""

    code: str | None = "CodeMismatchException"

    def __init__(self, data: CodeMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CodeMismatchException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CodeMismatchException":
        return cls(deserialize_aws_json_1_1(data))
