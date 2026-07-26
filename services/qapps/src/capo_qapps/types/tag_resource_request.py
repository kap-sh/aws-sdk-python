"""Generated from Smithy shape ``com.amazonaws.qapps#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.amazon_resource_name
    import capo_qapps.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_qapps.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_qapps.types.tags.Tags"
    """<p>The tags to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_qapps.types.tags

    out["tags"] = capo_qapps.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_qapps.types.tags

        out["tags"] = capo_qapps.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
