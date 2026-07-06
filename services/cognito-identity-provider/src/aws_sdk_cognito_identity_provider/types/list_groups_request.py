"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.pagination_key
    import aws_sdk_cognito_identity_provider.types.query_limit_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class ListGroupsRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to list user groups.</p>"""
    limit: NotRequired[
        "aws_sdk_cognito_identity_provider.types.query_limit_type.QueryLimitType"
    ]
    """<p>The maximum number of groups that you want Amazon Cognito to return in the response.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsRequest:
    out: ListGroupsRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("ListGroupsRequest.user_pool_id required")
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
