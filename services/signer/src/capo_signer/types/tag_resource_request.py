"""Generated from Smithy shape ``com.amazonaws.signer#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_signer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signer.types.string
    import capo_signer.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_signer.types.string.String"
    """<p>The Amazon Resource Name (ARN) for the signing profile.</p>"""
    tags: "capo_signer.types.tag_map.TagMap"
    """<p>One or more tags to be associated with the signing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_signer.types.tag_map

    out["tags"] = capo_signer.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_signer.types.tag_map

        out["tags"] = capo_signer.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
