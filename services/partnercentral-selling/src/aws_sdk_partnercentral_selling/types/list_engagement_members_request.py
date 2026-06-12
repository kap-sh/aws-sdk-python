"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementMembersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier
    import aws_sdk_partnercentral_selling.types.member_page_size


class ListEngagementMembersRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>The catalog related to the request.</p>"""
    identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier"
    """<p>Identifier of the Engagement record to retrieve members from.</p>"""
    max_results: "aws_sdk_partnercentral_selling.types.member_page_size.MemberPageSize"
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementMembersRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    out["MaxResults"] = value.get("max_results", 5)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementMembersRequest:
    out: ListEngagementMembersRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListEngagementMembersRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("ListEngagementMembersRequest.identifier required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 5
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
