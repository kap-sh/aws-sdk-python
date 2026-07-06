"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DeveloperUserAlreadyRegisteredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.string


class DeveloperUserAlreadyRegisteredException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cognito_identity.types.string.String"]
    """<p>This developer user identifier is already registered with Cognito.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeveloperUserAlreadyRegisteredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeveloperUserAlreadyRegisteredException_:
    out: DeveloperUserAlreadyRegisteredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DeveloperUserAlreadyRegisteredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentity#DeveloperUserAlreadyRegisteredException``."""

    code: str | None = "DeveloperUserAlreadyRegisteredException"

    def __init__(self, data: DeveloperUserAlreadyRegisteredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeveloperUserAlreadyRegisteredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DeveloperUserAlreadyRegisteredException":
        return cls(deserialize_aws_json_1_1(data))
