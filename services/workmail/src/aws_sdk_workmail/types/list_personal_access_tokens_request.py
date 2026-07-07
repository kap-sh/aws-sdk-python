"""Generated from Smithy shape ``com.amazonaws.workmail#ListPersonalAccessTokensRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.max_results
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.organization_id


class ListPersonalAccessTokensRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p> The Organization ID. </p>"""
    user_id: NotRequired["aws_sdk_workmail.types.entity_identifier.EntityIdentifier"]
    """<p> The WorkMail User ID. </p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p> The token from the previous response to query the next page.</p>"""
    max_results: NotRequired["aws_sdk_workmail.types.max_results.MaxResults"]
    """<p> The maximum amount of items that should be returned in a response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPersonalAccessTokensRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPersonalAccessTokensRequest:
    out: ListPersonalAccessTokensRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "ListPersonalAccessTokensRequest.organization_id required"
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
