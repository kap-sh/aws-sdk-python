"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolClientDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.client_name_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class UserPoolClientDescription(TypedDict, closed=True):
    client_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The app client ID.</p>"""
    user_pool_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that's associated with the app client.</p>"""
    client_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_name_type.ClientNameType"
    ]
    """<p>The app client name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolClientDescription) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "client_name" in value:
        out["ClientName"] = value["client_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolClientDescription:
    out: UserPoolClientDescription = {}  # type: ignore[typeddict-item]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    if "ClientName" in data:
        out["client_name"] = data["ClientName"]
    return out
