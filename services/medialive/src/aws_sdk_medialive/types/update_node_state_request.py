"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateNodeStateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.update_node_state_shape


class UpdateNodeStateRequest(TypedDict):
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster"""
    node_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the node."""
    state: NotRequired[
        "aws_sdk_medialive.types.update_node_state_shape.UpdateNodeStateShape"
    ]
    """The state to apply to the Node. Set to ACTIVE (COMMISSIONED) to indicate that the Node is deployable. MediaLive Anywhere will consider this node it needs a Node to run a Channel on, or when it needs a Node to promote from a backup node to an active node. Set to DRAINING to isolate the Node so that MediaLive Anywhere won't use it."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodeStateRequest) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_medialive.types.update_node_state_shape

        out["state"] = aws_sdk_medialive.types.update_node_state_shape.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNodeStateRequest:
    out: UpdateNodeStateRequest = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_medialive.types.update_node_state_shape

        out["state"] = aws_sdk_medialive.types.update_node_state_shape.deserialize_json(
            data["state"]
        )
    return out
