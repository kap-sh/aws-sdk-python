"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#InternalErrorException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.string


class InternalErrorException_(TypedDict):
    message: NotRequired["aws_sdk_cognito_identity.types.string.String"]
    """<p>The message returned by an InternalErrorException.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentity#InternalErrorException``."""

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
