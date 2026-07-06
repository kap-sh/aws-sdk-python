"""Generated from Smithy shape ``com.amazonaws.budgets#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_budgets.types.resource_tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_tags: NotRequired[
        "aws_sdk_budgets.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import aws_sdk_budgets.types.resource_tag_list

        out["ResourceTags"] = (
            aws_sdk_budgets.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceTags" in data:
        import aws_sdk_budgets.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_budgets.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out
