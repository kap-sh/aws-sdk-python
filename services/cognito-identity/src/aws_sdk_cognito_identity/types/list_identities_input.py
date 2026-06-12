"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListIdentitiesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.hide_disabled
    import aws_sdk_cognito_identity.types.identity_pool_id
    import aws_sdk_cognito_identity.types.pagination_key
    import aws_sdk_cognito_identity.types.query_limit


class ListIdentitiesInput(TypedDict):
    identity_pool_id: "aws_sdk_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    max_results: "aws_sdk_cognito_identity.types.query_limit.QueryLimit"
    """<p>The maximum number of identities to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity.types.pagination_key.PaginationKey"
    ]
    """<p>A pagination token.</p>"""
    hide_disabled: "aws_sdk_cognito_identity.types.hide_disabled.HideDisabled"
    """<p>An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIdentitiesInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["HideDisabled"] = value.get("hide_disabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIdentitiesInput:
    out: ListIdentitiesInput = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError("ListIdentitiesInput.identity_pool_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        raise DeserializationError("ListIdentitiesInput.max_results required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "HideDisabled" in data:
        out["hide_disabled"] = data["HideDisabled"]
    else:
        out["hide_disabled"] = False
    return out
