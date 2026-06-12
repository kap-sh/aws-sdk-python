"""Generated from Smithy shape ``com.amazonaws.opensearch#CognitoOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.identity_pool_id
    import aws_sdk_opensearch.types.role_arn
    import aws_sdk_opensearch.types.user_pool_id


class CognitoOptions(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards.</p>"""
    user_pool_id: NotRequired["aws_sdk_opensearch.types.user_pool_id.UserPoolId"]
    """<p>The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.</p>"""
    identity_pool_id: NotRequired[
        "aws_sdk_opensearch.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.</p>"""
    role_arn: NotRequired["aws_sdk_opensearch.types.role_arn.RoleArn"]
    """<p>The <code>AmazonOpenSearchServiceCognitoAccess</code> role that allows OpenSearch Service to configure your user pool and identity pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CognitoOptions:
    out: CognitoOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
