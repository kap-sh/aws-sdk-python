"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.next_page_token
    import capo_bcm_data_exports.types.resource_tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_tags: NotRequired[
        "capo_bcm_data_exports.types.resource_tag_list.ResourceTagList"
    ]
    """<p>An optional list of tags to associate with the specified export. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""
    next_token: NotRequired["capo_bcm_data_exports.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import capo_bcm_data_exports.types.resource_tag_list

        out["ResourceTags"] = (
            capo_bcm_data_exports.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceTags" in data:
        import capo_bcm_data_exports.types.resource_tag_list

        out["resource_tags"] = (
            capo_bcm_data_exports.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
