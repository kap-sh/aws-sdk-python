"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_global_accelerator.types.tags.Tags"]
    """<p>Root level tag for the Tags parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_global_accelerator.types.tags

        out["Tags"] = capo_global_accelerator.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_global_accelerator.types.tags

        out["tags"] = capo_global_accelerator.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
