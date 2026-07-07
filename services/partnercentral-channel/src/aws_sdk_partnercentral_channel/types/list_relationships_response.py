"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListRelationshipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.next_token
    import aws_sdk_partnercentral_channel.types.relationship_summaries


class ListRelationshipsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_summaries.RelationshipSummaries"
    ]
    """<p>List of relationships matching the criteria.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results, if available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRelationshipsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_partnercentral_channel.types.relationship_summaries

        out["items"] = (
            aws_sdk_partnercentral_channel.types.relationship_summaries.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRelationshipsResponse:
    out: ListRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_partnercentral_channel.types.relationship_summaries

        out["items"] = (
            aws_sdk_partnercentral_channel.types.relationship_summaries.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
