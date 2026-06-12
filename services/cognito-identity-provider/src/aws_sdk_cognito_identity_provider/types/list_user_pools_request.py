"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserPoolsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.pagination_key_type
    import aws_sdk_cognito_identity_provider.types.pool_query_limit_type


class ListUserPoolsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""
    max_results: "aws_sdk_cognito_identity_provider.types.pool_query_limit_type.PoolQueryLimitType"
    """<p>The maximum number of user pools that you want Amazon Cognito to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserPoolsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserPoolsRequest:
    out: ListUserPoolsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        raise DeserializationError("ListUserPoolsRequest.max_results required")
    return out
