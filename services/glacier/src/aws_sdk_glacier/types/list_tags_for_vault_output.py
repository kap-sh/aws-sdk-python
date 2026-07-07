"""Generated from Smithy shape ``com.amazonaws.glacier#ListTagsForVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.tag_map


class ListTagsForVaultOutput(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_glacier.types.tag_map.TagMap"]
    """<p>The tags attached to the vault. Each tag is composed of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForVaultOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_glacier.types.tag_map

        out["Tags"] = aws_sdk_glacier.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForVaultOutput:
    out: ListTagsForVaultOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_glacier.types.tag_map

        out["tags"] = aws_sdk_glacier.types.tag_map.deserialize_json(data["Tags"])
    return out
