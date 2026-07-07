"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserPoolClientsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.pagination_key
    import aws_sdk_cognito_identity_provider.types.user_pool_client_list_type


class ListUserPoolClientsResponse(TypedDict, closed=True):
    user_pool_clients: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_client_list_type.UserPoolClientListType"
    ]
    """<p>An array of app clients and their details. Includes app client ID and name.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserPoolClientsResponse) -> dict:
    out: dict = {}
    if "user_pool_clients" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_client_list_type

        out["UserPoolClients"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_client_list_type.serialize_aws_json_1_1(
                value["user_pool_clients"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserPoolClientsResponse:
    out: ListUserPoolClientsResponse = {}  # type: ignore[typeddict-item]
    if "UserPoolClients" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_client_list_type

        out["user_pool_clients"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_client_list_type.deserialize_aws_json_1_1(
                data["UserPoolClients"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
