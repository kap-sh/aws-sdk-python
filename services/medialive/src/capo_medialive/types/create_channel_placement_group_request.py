"""Generated from Smithy shape ``com.amazonaws.medialive#CreateChannelPlacementGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__string
    import capo_medialive.types.tags


class CreateChannelPlacementGroupRequest(TypedDict, closed=True):
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive."""
    nodes: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """An array of one ID for the Node that you want to associate with the ChannelPlacementGroup. (You can't associate more than one Node with the ChannelPlacementGroup.) The Node and the ChannelPlacementGroup must be in the same Cluster."""
    request_id: NotRequired["capo_medialive.types.__string.__string"]
    """An ID that you assign to a create request. This ID ensures idempotency when creating resources. the request."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelPlacementGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "nodes" in value:
        import capo_medialive.types.__list_of__string

        out["nodes"] = capo_medialive.types.__list_of__string.serialize_json(
            value["nodes"]
        )
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateChannelPlacementGroupRequest:
    out: CreateChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nodes" in data:
        import capo_medialive.types.__list_of__string

        out["nodes"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["nodes"]
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    return out
