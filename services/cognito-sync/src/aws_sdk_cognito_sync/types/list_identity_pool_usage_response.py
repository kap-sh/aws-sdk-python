"""Generated from Smithy shape ``com.amazonaws.cognitosync#ListIdentityPoolUsageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.identity_pool_usage_list
    import aws_sdk_cognito_sync.types.integer
    import aws_sdk_cognito_sync.types.string


class ListIdentityPoolUsageResponse(TypedDict):
    identity_pool_usages: NotRequired[
        "aws_sdk_cognito_sync.types.identity_pool_usage_list.IdentityPoolUsageList"
    ]
    """Usage information for the identity pools."""
    max_results: "aws_sdk_cognito_sync.types.integer.Integer"
    """The maximum number of results to be returned."""
    count: "aws_sdk_cognito_sync.types.integer.Integer"
    """Total number of identities for the identity pool."""
    next_token: NotRequired["aws_sdk_cognito_sync.types.string.String"]
    """A pagination token for obtaining the next page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityPoolUsageResponse) -> dict:
    out: dict = {}
    if "identity_pool_usages" in value:
        import aws_sdk_cognito_sync.types.identity_pool_usage_list

        out["IdentityPoolUsages"] = (
            aws_sdk_cognito_sync.types.identity_pool_usage_list.serialize_json(
                value["identity_pool_usages"]
            )
        )
    out["MaxResults"] = value.get("max_results", 0)
    out["Count"] = value.get("count", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdentityPoolUsageResponse:
    out: ListIdentityPoolUsageResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolUsages" in data:
        import aws_sdk_cognito_sync.types.identity_pool_usage_list

        out["identity_pool_usages"] = (
            aws_sdk_cognito_sync.types.identity_pool_usage_list.deserialize_json(
                data["IdentityPoolUsages"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
