"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListWebAuthnCredentialsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.pagination_key
    import aws_sdk_cognito_identity_provider.types.token_model_type
    import aws_sdk_cognito_identity_provider.types.web_authn_credentials_query_limit_type


class ListWebAuthnCredentialsRequest(TypedDict):
    access_token: (
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    )
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""
    max_results: NotRequired[
        "aws_sdk_cognito_identity_provider.types.web_authn_credentials_query_limit_type.WebAuthnCredentialsQueryLimitType"
    ]
    """<p>The maximum number of the user's passkey credentials that you want to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebAuthnCredentialsRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebAuthnCredentialsRequest:
    out: ListWebAuthnCredentialsRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError(
            "ListWebAuthnCredentialsRequest.access_token required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
