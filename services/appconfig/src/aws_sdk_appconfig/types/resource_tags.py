"""Generated from Smithy shape ``com.amazonaws.appconfig#ResourceTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.tag_map


class ResourceTags(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to AppConfig resources. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTags) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_appconfig.types.tag_map

        out["Tags"] = aws_sdk_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ResourceTags:
    out: ResourceTags = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_appconfig.types.tag_map

        out["tags"] = aws_sdk_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
