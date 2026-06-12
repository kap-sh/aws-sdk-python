"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListIdentityPoolsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.pagination_key
    import aws_sdk_cognito_identity.types.query_limit


class ListIdentityPoolsInput(TypedDict):
    max_results: "aws_sdk_cognito_identity.types.query_limit.QueryLimit"
    """<p>The maximum number of identities to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity.types.pagination_key.PaginationKey"
    ]
    """<p>A pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIdentityPoolsInput) -> dict:
    out: dict = {}
    out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIdentityPoolsInput:
    out: ListIdentityPoolsInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        raise DeserializationError("ListIdentityPoolsInput.max_results required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
