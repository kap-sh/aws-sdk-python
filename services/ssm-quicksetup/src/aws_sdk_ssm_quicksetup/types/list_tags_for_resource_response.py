"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_ssm_quicksetup.types.tags.Tags"]
    """<p>Key-value pairs of metadata assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_ssm_quicksetup.types.tags

        out["Tags"] = aws_sdk_ssm_quicksetup.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_ssm_quicksetup.types.tags

        out["tags"] = aws_sdk_ssm_quicksetup.types.tags.deserialize_json(data["Tags"])
    return out
