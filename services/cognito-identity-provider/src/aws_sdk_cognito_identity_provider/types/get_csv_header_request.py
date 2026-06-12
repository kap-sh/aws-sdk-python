"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetCSVHeaderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class GetCSVHeaderRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that you want to import users into.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCSVHeaderRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCSVHeaderRequest:
    out: GetCSVHeaderRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("GetCSVHeaderRequest.user_pool_id required")
    return out
