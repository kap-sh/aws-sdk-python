"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#FeatureUnavailableInTierException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.message_type


class FeatureUnavailableInTierException_(TypedDict):
    message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureUnavailableInTierException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureUnavailableInTierException_:
    out: FeatureUnavailableInTierException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class FeatureUnavailableInTierException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#FeatureUnavailableInTierException``."""

    code: str | None = "FeatureUnavailableInTierException"

    def __init__(self, data: FeatureUnavailableInTierException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FeatureUnavailableInTierException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FeatureUnavailableInTierException":
        return cls(deserialize_aws_json_1_1(data))
