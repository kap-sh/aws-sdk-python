"""Generated from Smithy shape ``com.amazonaws.amplifybackend#LoginAuthConfigReqObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class LoginAuthConfigReqObj(TypedDict, closed=True):
    aws_cognito_identity_pool_id: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The Amazon Cognito identity pool ID used for the Amplify Admin UI login authorization.</p>"""
    aws_cognito_region: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The AWS Region for the Amplify Admin UI login.</p>"""
    aws_user_pools_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The Amazon Cognito user pool ID used for Amplify Admin UI login authentication.</p>"""
    aws_user_pools_web_client_id: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The web client ID for the Amazon Cognito user pools.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoginAuthConfigReqObj) -> dict:
    out: dict = {}
    if "aws_cognito_identity_pool_id" in value:
        out["aws_cognito_identity_pool_id"] = value["aws_cognito_identity_pool_id"]
    if "aws_cognito_region" in value:
        out["aws_cognito_region"] = value["aws_cognito_region"]
    if "aws_user_pools_id" in value:
        out["aws_user_pools_id"] = value["aws_user_pools_id"]
    if "aws_user_pools_web_client_id" in value:
        out["aws_user_pools_web_client_id"] = value["aws_user_pools_web_client_id"]
    return out


def deserialize_json(data: dict) -> LoginAuthConfigReqObj:
    out: LoginAuthConfigReqObj = {}  # type: ignore[typeddict-item]
    if "aws_cognito_identity_pool_id" in data:
        out["aws_cognito_identity_pool_id"] = data["aws_cognito_identity_pool_id"]
    if "aws_cognito_region" in data:
        out["aws_cognito_region"] = data["aws_cognito_region"]
    if "aws_user_pools_id" in data:
        out["aws_user_pools_id"] = data["aws_user_pools_id"]
    if "aws_user_pools_web_client_id" in data:
        out["aws_user_pools_web_client_id"] = data["aws_user_pools_web_client_id"]
    return out
