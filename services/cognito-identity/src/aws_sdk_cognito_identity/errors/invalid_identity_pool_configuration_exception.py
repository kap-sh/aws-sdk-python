"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#InvalidIdentityPoolConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.string


class InvalidIdentityPoolConfigurationException_(TypedDict):
    message: NotRequired["aws_sdk_cognito_identity.types.string.String"]
    """<p>The message returned for an <code>InvalidIdentityPoolConfigurationException</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidIdentityPoolConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidIdentityPoolConfigurationException_:
    out: InvalidIdentityPoolConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidIdentityPoolConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentity#InvalidIdentityPoolConfigurationException``."""

    code: str | None = "InvalidIdentityPoolConfigurationException"

    def __init__(self, data: InvalidIdentityPoolConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidIdentityPoolConfigurationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InvalidIdentityPoolConfigurationException":
        return cls(deserialize_aws_json_1_1(data))
