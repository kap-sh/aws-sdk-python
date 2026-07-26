"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserPoolsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key_type
    import capo_cognito_identity_provider.types.user_pool_list_type


class ListUserPoolsResponse(TypedDict, closed=True):
    user_pools: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_list_type.UserPoolListType"
    ]
    """<p>An array of user pools and their configuration details.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserPoolsResponse) -> dict:
    out: dict = {}
    if "user_pools" in value:
        import capo_cognito_identity_provider.types.user_pool_list_type

        out["UserPools"] = (
            capo_cognito_identity_provider.types.user_pool_list_type.serialize_aws_json_1_1(
                value["user_pools"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserPoolsResponse:
    out: ListUserPoolsResponse = {}  # type: ignore[typeddict-item]
    if "UserPools" in data:
        import capo_cognito_identity_provider.types.user_pool_list_type

        out["user_pools"] = (
            capo_cognito_identity_provider.types.user_pool_list_type.deserialize_aws_json_1_1(
                data["UserPools"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
