"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_ssm_quicksetup.types.tags.Tags"]
    """<p>Key-value pairs of metadata assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_ssm_quicksetup.types.tags

        out["Tags"] = capo_ssm_quicksetup.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_ssm_quicksetup.types.tags

        out["tags"] = capo_ssm_quicksetup.types.tags.deserialize_json(data["Tags"])
    return out
