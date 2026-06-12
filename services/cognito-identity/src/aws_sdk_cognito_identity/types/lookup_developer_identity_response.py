"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#LookupDeveloperIdentityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.developer_user_identifier_list
    import aws_sdk_cognito_identity.types.identity_id
    import aws_sdk_cognito_identity.types.pagination_key


class LookupDeveloperIdentityResponse(TypedDict):
    identity_id: NotRequired["aws_sdk_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    developer_user_identifier_list: NotRequired[
        "aws_sdk_cognito_identity.types.developer_user_identifier_list.DeveloperUserIdentifierList"
    ]
    """<p>This is the list of developer user identifiers associated with an identity ID. Cognito supports the association of multiple developer user identifiers with an identity ID.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity.types.pagination_key.PaginationKey"
    ]
    """<p>A pagination token. The first call you make will have <code>NextToken</code> set to null. After that the service will return <code>NextToken</code> values as needed. For example, let's say you make a request with <code>MaxResults</code> set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupDeveloperIdentityResponse) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "developer_user_identifier_list" in value:
        import aws_sdk_cognito_identity.types.developer_user_identifier_list

        out["DeveloperUserIdentifierList"] = (
            aws_sdk_cognito_identity.types.developer_user_identifier_list.serialize_aws_json_1_1(
                value["developer_user_identifier_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LookupDeveloperIdentityResponse:
    out: LookupDeveloperIdentityResponse = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "DeveloperUserIdentifierList" in data:
        import aws_sdk_cognito_identity.types.developer_user_identifier_list

        out["developer_user_identifier_list"] = (
            aws_sdk_cognito_identity.types.developer_user_identifier_list.deserialize_aws_json_1_1(
                data["DeveloperUserIdentifierList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
