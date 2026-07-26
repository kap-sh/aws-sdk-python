"""Generated from Smithy shape ``com.amazonaws.connectcases#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.arn
    import capo_connectcases.types.tags


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_connectcases.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN)</p>"""
    tags: "capo_connectcases.types.tags.Tags"
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.tags

    out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
