"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) to use to tag a resource.</p>"""
    tags: "capo_amplifyuibuilder.types.tags.Tags"
    """<p>A list of tag key value pairs for a specified Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.tags

    out["tags"] = capo_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
