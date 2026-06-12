"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.page_size
    import aws_sdk_cost_explorer.types.tag_list


class GetTagsResponse(TypedDict):
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    tags: "aws_sdk_cost_explorer.types.tag_list.TagList"
    """<p>The tags that match your request.</p>"""
    return_size: "aws_sdk_cost_explorer.types.page_size.PageSize"
    """<p>The number of query results that Amazon Web Services returns at a time.</p>"""
    total_size: "aws_sdk_cost_explorer.types.page_size.PageSize"
    """<p>The total number of query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagsResponse) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    import aws_sdk_cost_explorer.types.tag_list

    out["Tags"] = aws_sdk_cost_explorer.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    out["ReturnSize"] = value["return_size"]
    out["TotalSize"] = value["total_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagsResponse:
    out: GetTagsResponse = {}  # type: ignore[typeddict-item]
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "Tags" in data:
        import aws_sdk_cost_explorer.types.tag_list

        out["tags"] = aws_sdk_cost_explorer.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("GetTagsResponse.tags required")
    if "ReturnSize" in data:
        out["return_size"] = data["ReturnSize"]
    else:
        raise DeserializationError("GetTagsResponse.return_size required")
    if "TotalSize" in data:
        out["total_size"] = data["TotalSize"]
    else:
        raise DeserializationError("GetTagsResponse.total_size required")
    return out
