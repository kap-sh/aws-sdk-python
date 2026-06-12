"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.next_token
    import aws_sdk_route53resolver.types.tag_list


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_route53resolver.types.tag_list.TagList"]
    """<p>The tags that are associated with the resource that you specified in the <code>ListTagsForResource</code> request.</p>"""
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> tags match the specified criteria, you can submit another <code>ListTagsForResource</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_route53resolver.types.tag_list

        out["Tags"] = aws_sdk_route53resolver.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_route53resolver.types.tag_list

        out["tags"] = aws_sdk_route53resolver.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
