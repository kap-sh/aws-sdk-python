"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_application_auto_scaling.types.tag_map.TagMap"]
    """<p>A list of tags. Each tag consists of a tag key and a tag value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_application_auto_scaling.types.tag_map

        out["Tags"] = (
            capo_application_auto_scaling.types.tag_map.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_application_auto_scaling.types.tag_map

        out["tags"] = (
            capo_application_auto_scaling.types.tag_map.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
