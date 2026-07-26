"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateNodeStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.update_node_state_shape


class UpdateNodeStateRequest(TypedDict, closed=True):
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster"""
    node_id: "capo_medialive.types.__string.__string"
    """The ID of the node."""
    state: NotRequired[
        "capo_medialive.types.update_node_state_shape.UpdateNodeStateShape"
    ]
    """The state to apply to the Node. Set to ACTIVE (COMMISSIONED) to indicate that the Node is deployable. MediaLive Anywhere will consider this node it needs a Node to run a Channel on, or when it needs a Node to promote from a backup node to an active node. Set to DRAINING to isolate the Node so that MediaLive Anywhere won't use it."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodeStateRequest) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_medialive.types.update_node_state_shape

        out["state"] = capo_medialive.types.update_node_state_shape.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNodeStateRequest:
    out: UpdateNodeStateRequest = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_medialive.types.update_node_state_shape

        out["state"] = capo_medialive.types.update_node_state_shape.deserialize_json(
            data["state"]
        )
    return out
