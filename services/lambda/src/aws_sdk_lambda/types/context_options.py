"""Generated from Smithy shape ``com.amazonaws.lambda#ContextOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.replay_children


class ContextOptions(TypedDict):
    replay_children: NotRequired["aws_sdk_lambda.types.replay_children.ReplayChildren"]
    """<p>Whether the state data of children of the completed context should be included in the invoke payload and <code>GetDurableExecutionState</code> response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextOptions) -> dict:
    out: dict = {}
    if "replay_children" in value:
        out["ReplayChildren"] = value["replay_children"]
    return out


def deserialize_json(data: dict) -> ContextOptions:
    out: ContextOptions = {}  # type: ignore[typeddict-item]
    if "ReplayChildren" in data:
        out["replay_children"] = data["ReplayChildren"]
    return out
