"""Generated from Smithy shape ``com.amazonaws.detective#CreateGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.tag_map


class CreateGraphRequest(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_detective.types.tag_map.TagMap"]
    """<p>The tags to assign to the new behavior graph. You can add up to 50 tags. For each tag, you provide the tag key and the tag value. Each tag key can contain up to 128 characters. Each tag value can contain up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_detective.types.tag_map

        out["Tags"] = aws_sdk_detective.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateGraphRequest:
    out: CreateGraphRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_detective.types.tag_map

        out["tags"] = aws_sdk_detective.types.tag_map.deserialize_json(data["Tags"])
    return out
