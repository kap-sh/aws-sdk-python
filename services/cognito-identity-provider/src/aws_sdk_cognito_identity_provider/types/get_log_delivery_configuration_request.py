"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetLogDeliveryConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class GetLogDeliveryConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that has the logging configuration that you want to view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogDeliveryConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogDeliveryConfigurationRequest:
    out: GetLogDeliveryConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "GetLogDeliveryConfigurationRequest.user_pool_id required"
        )
    return out
