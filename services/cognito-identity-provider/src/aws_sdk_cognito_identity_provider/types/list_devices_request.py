"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListDevicesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.query_limit_type
    import aws_sdk_cognito_identity_provider.types.search_pagination_token_type
    import aws_sdk_cognito_identity_provider.types.token_model_type


class ListDevicesRequest(TypedDict):
    access_token: (
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    )
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    limit: NotRequired[
        "aws_sdk_cognito_identity_provider.types.query_limit_type.QueryLimitType"
    ]
    """<p>The maximum number of devices that you want Amazon Cognito to return in the response.</p>"""
    pagination_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.search_pagination_token_type.SearchPaginationTokenType"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicesRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicesRequest:
    out: ListDevicesRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("ListDevicesRequest.access_token required")
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "PaginationToken" in data:
        out["pagination_token"] = data["PaginationToken"]
    return out
