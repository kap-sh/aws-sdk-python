"""Generated from Smithy shape ``com.amazonaws.tnb#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.tag_map
    import capo_tnb.types.tnb_resource_arn


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_tnb.types.tnb_resource_arn.TNBResourceArn"
    """<p>Resource ARN.</p>"""
    tags: "capo_tnb.types.tag_map.TagMap"
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_tnb.types.tag_map

    out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
