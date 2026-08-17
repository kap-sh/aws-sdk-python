"""Generated from Smithy shape ``com.amazonaws.lambda#ContextOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.replay_children


class ContextOptions(TypedDict, closed=True):
    replay_children: NotRequired["capo_lambda.types.replay_children.ReplayChildren"]
    """<p>Whether the state data of children of the completed context should be included in the invoke payload and <code>GetDurableExecutionState</code> response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextOptions) -> dict:
    out: dict = {}
    if "replay_children" in value:
        out["ReplayChildren"] = value["replay_children"]
    return out


def deserialize_json(data: dict) -> ContextOptions:
    out: ContextOptions = {}  # type: ignore[typeddict-item]
    if data.get("ReplayChildren") is not None:
        out["replay_children"] = data["ReplayChildren"]
    return out
