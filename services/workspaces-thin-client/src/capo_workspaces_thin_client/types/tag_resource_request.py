"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces_thin_client.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "capo_workspaces_thin_client.types.tags_map.TagsMap"
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_workspaces_thin_client.types.tags_map

    out["tags"] = capo_workspaces_thin_client.types.tags_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_workspaces_thin_client.types.tags_map

        out["tags"] = capo_workspaces_thin_client.types.tags_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
