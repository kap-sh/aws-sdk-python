"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeResourceServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.resource_server_identifier_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class DescribeResourceServerRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that hosts the resource server.</p>"""
    identifier: "aws_sdk_cognito_identity_provider.types.resource_server_identifier_type.ResourceServerIdentifierType"
    """<p>A unique resource server identifier for the resource server. The identifier can be an API friendly name like <code>solar-system-data</code>. You can also set an API URL like <code>https://solar-system-data-api.example.com</code> as your identifier.</p> <p>Amazon Cognito represents scopes in the access token in the format <code>$resource-server-identifier/$scope</code>. Longer scope-identifier strings increase the size of your access tokens.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourceServerRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourceServerRequest:
    out: DescribeResourceServerRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DescribeResourceServerRequest.user_pool_id required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("DescribeResourceServerRequest.identifier required")
    return out
