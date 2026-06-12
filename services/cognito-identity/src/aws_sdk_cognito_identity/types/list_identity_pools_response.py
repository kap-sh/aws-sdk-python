"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListIdentityPoolsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_pools_list
    import aws_sdk_cognito_identity.types.pagination_key


class ListIdentityPoolsResponse(TypedDict):
    identity_pools: NotRequired[
        "aws_sdk_cognito_identity.types.identity_pools_list.IdentityPoolsList"
    ]
    """<p>The identity pools returned by the ListIdentityPools action.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity.types.pagination_key.PaginationKey"
    ]
    """<p>A pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIdentityPoolsResponse) -> dict:
    out: dict = {}
    if "identity_pools" in value:
        import aws_sdk_cognito_identity.types.identity_pools_list

        out["IdentityPools"] = (
            aws_sdk_cognito_identity.types.identity_pools_list.serialize_aws_json_1_1(
                value["identity_pools"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIdentityPoolsResponse:
    out: ListIdentityPoolsResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPools" in data:
        import aws_sdk_cognito_identity.types.identity_pools_list

        out["identity_pools"] = (
            aws_sdk_cognito_identity.types.identity_pools_list.deserialize_aws_json_1_1(
                data["IdentityPools"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
