"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.pagination_token
    import aws_sdk_network_firewall.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The tags that are associated with the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
