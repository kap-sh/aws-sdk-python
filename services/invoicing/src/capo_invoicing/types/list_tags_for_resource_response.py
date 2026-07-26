"""Generated from Smithy shape ``com.amazonaws.invoicing#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.resource_tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_tags: NotRequired["capo_invoicing.types.resource_tag_list.ResourceTagList"]
    """<p> Adds a tag to a resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import capo_invoicing.types.resource_tag_list

        out["ResourceTags"] = (
            capo_invoicing.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceTags" in data:
        import capo_invoicing.types.resource_tag_list

        out["resource_tags"] = (
            capo_invoicing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["ResourceTags"]
            )
        )
    return out
