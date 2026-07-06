"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListIdentitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identities_list
    import aws_sdk_cognito_identity.types.identity_pool_id
    import aws_sdk_cognito_identity.types.pagination_key


class ListIdentitiesResponse(TypedDict, closed=True):
    identity_pool_id: NotRequired[
        "aws_sdk_cognito_identity.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    identities: NotRequired[
        "aws_sdk_cognito_identity.types.identities_list.IdentitiesList"
    ]
    """<p>An object containing a set of identities and associated mappings.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity.types.pagination_key.PaginationKey"
    ]
    """<p>A pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIdentitiesResponse) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "identities" in value:
        import aws_sdk_cognito_identity.types.identities_list

        out["Identities"] = (
            aws_sdk_cognito_identity.types.identities_list.serialize_aws_json_1_1(
                value["identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIdentitiesResponse:
    out: ListIdentitiesResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "Identities" in data:
        import aws_sdk_cognito_identity.types.identities_list

        out["identities"] = (
            aws_sdk_cognito_identity.types.identities_list.deserialize_aws_json_1_1(
                data["Identities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
