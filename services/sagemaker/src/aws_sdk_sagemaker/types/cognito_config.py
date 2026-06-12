"""Generated from Smithy shape ``com.amazonaws.sagemaker#CognitoConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.client_id
    import aws_sdk_sagemaker.types.cognito_user_pool


class CognitoConfig(TypedDict):
    user_pool: NotRequired["aws_sdk_sagemaker.types.cognito_user_pool.CognitoUserPool"]
    """<p>A <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html\"> user pool</a> is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers.</p>"""
    client_id: NotRequired["aws_sdk_sagemaker.types.client_id.ClientId"]
    """<p>The client ID for your Amazon Cognito user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CognitoConfig) -> dict:
    out: dict = {}
    if "user_pool" in value:
        out["UserPool"] = value["user_pool"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CognitoConfig:
    out: CognitoConfig = {}  # type: ignore[typeddict-item]
    if "UserPool" in data:
        out["user_pool"] = data["UserPool"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    return out
