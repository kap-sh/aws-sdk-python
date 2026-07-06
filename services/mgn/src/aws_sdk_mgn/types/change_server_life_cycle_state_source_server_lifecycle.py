"""Generated from Smithy shape ``com.amazonaws.mgn#ChangeServerLifeCycleStateSourceServerLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle_state


class ChangeServerLifeCycleStateSourceServerLifecycle(TypedDict, closed=True):
    state: "aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle_state.ChangeServerLifeCycleStateSourceServerLifecycleState"
    """<p>The request to change the source server migration lifecycle state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeServerLifeCycleStateSourceServerLifecycle) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> ChangeServerLifeCycleStateSourceServerLifecycle:
    out: ChangeServerLifeCycleStateSourceServerLifecycle = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError(
            "ChangeServerLifeCycleStateSourceServerLifecycle.state required"
        )
    return out
