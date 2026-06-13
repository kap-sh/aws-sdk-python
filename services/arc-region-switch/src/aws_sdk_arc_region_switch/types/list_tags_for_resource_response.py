"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.tags


class ListTagsForResourceResponse(TypedDict):
    resource_tags: NotRequired["aws_sdk_arc_region_switch.types.tags.Tags"]
    """<p>The tags for a resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import aws_sdk_arc_region_switch.types.tags

        out["resourceTags"] = (
            aws_sdk_arc_region_switch.types.tags.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "resourceTags" in data:
        import aws_sdk_arc_region_switch.types.tags

        out["resource_tags"] = (
            aws_sdk_arc_region_switch.types.tags.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
