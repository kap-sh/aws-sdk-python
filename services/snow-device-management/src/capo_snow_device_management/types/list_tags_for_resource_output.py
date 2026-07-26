"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.tag_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_snow_device_management.types.tag_map.TagMap"]
    """<p>The list of tags for the device or task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_snow_device_management.types.tag_map

        out["tags"] = capo_snow_device_management.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_snow_device_management.types.tag_map

        out["tags"] = capo_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
