"""Generated from Smithy shape ``com.amazonaws.billing#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billing.types.resource_tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_tags: NotRequired[
        "aws_sdk_billing.types.resource_tag_list.ResourceTagList"
    ]
    """<p> A list of tag key value pairs that are associated with the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import aws_sdk_billing.types.resource_tag_list

        out["resourceTags"] = (
            aws_sdk_billing.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "resourceTags" in data:
        import aws_sdk_billing.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_billing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
