"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.resource_tag_list
    import capo_cloudtrail.types.string


class ListTagsResponse(TypedDict, closed=True):
    resource_tag_list: NotRequired[
        "capo_cloudtrail.types.resource_tag_list.ResourceTagList"
    ]
    """<p>A list of resource tags.</p>"""
    next_token: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "resource_tag_list" in value:
        import capo_cloudtrail.types.resource_tag_list

        out["ResourceTagList"] = (
            capo_cloudtrail.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tag_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceTagList" in data:
        import capo_cloudtrail.types.resource_tag_list

        out["resource_tag_list"] = (
            capo_cloudtrail.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTagList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
