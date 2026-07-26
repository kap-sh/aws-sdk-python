"""Generated from Smithy shape ``com.amazonaws.grafana#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource the tag is associated with.</p>"""
    tags: "capo_grafana.types.tag_map.TagMap"
    """<p>The list of tag keys and values to associate with the resource. You can associate tag keys only, tags (key and values) only or a combination of tag keys and tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_grafana.types.tag_map

    out["tags"] = capo_grafana.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_grafana.types.tag_map

        out["tags"] = capo_grafana.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
