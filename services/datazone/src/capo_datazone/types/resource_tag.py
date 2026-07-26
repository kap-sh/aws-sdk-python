"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.resource_tag_source
    import capo_datazone.types.tag_key
    import capo_datazone.types.tag_value


class ResourceTag(TypedDict, closed=True):
    key: "capo_datazone.types.tag_key.TagKey"
    """<p>The key of the resource tag of the project.</p>"""
    value: "capo_datazone.types.tag_value.TagValue"
    """<p>The value of the resource tag of the project.</p>"""
    source: "capo_datazone.types.resource_tag_source.ResourceTagSource"
    """<p>The source of the resource tag of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    import capo_datazone.types.resource_tag_source

    out["source"] = capo_datazone.types.resource_tag_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ResourceTag.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ResourceTag.value required")
    if "source" in data:
        import capo_datazone.types.resource_tag_source

        out["source"] = capo_datazone.types.resource_tag_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("ResourceTag.source required")
    return out
