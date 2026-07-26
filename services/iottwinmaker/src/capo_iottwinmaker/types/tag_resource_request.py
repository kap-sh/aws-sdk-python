"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.tag_map
    import capo_iottwinmaker.types.twin_maker_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the resource.</p>"""
    tags: "capo_iottwinmaker.types.tag_map.TagMap"
    """<p>Metadata to add to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import capo_iottwinmaker.types.tag_map

    out["tags"] = capo_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
