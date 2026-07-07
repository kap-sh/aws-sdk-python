"""Generated from Smithy shape ``com.amazonaws.sagemaker#CognitoMemberDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.client_id
    import aws_sdk_sagemaker.types.cognito_user_group
    import aws_sdk_sagemaker.types.cognito_user_pool


class CognitoMemberDefinition(TypedDict, closed=True):
    user_pool: NotRequired["aws_sdk_sagemaker.types.cognito_user_pool.CognitoUserPool"]
    """<p>An identifier for a user pool. The user pool must be in the same region as the service that you are calling.</p>"""
    user_group: NotRequired[
        "aws_sdk_sagemaker.types.cognito_user_group.CognitoUserGroup"
    ]
    """<p>An identifier for a user group.</p>"""
    client_id: NotRequired["aws_sdk_sagemaker.types.client_id.ClientId"]
    """<p>An identifier for an application client. You must create the app client ID using Amazon Cognito.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CognitoMemberDefinition) -> dict:
    out: dict = {}
    if "user_pool" in value:
        out["UserPool"] = value["user_pool"]
    if "user_group" in value:
        out["UserGroup"] = value["user_group"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CognitoMemberDefinition:
    out: CognitoMemberDefinition = {}  # type: ignore[typeddict-item]
    if "UserPool" in data:
        out["user_pool"] = data["UserPool"]
    if "UserGroup" in data:
        out["user_group"] = data["UserGroup"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    return out
