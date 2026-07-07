"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CognitoOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.identity_pool_id
    import aws_sdk_elasticsearch_service.types.role_arn
    import aws_sdk_elasticsearch_service.types.user_pool_id


class CognitoOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>Specifies the option to enable Cognito for Kibana authentication.</p>"""
    user_pool_id: NotRequired[
        "aws_sdk_elasticsearch_service.types.user_pool_id.UserPoolId"
    ]
    """<p>Specifies the Cognito user pool ID for Kibana authentication.</p>"""
    identity_pool_id: NotRequired[
        "aws_sdk_elasticsearch_service.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>Specifies the Cognito identity pool ID for Kibana authentication.</p>"""
    role_arn: NotRequired["aws_sdk_elasticsearch_service.types.role_arn.RoleArn"]
    """<p>Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.</p>"""


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
