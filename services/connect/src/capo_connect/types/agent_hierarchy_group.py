"""Generated from Smithy shape ``com.amazonaws.connect#AgentHierarchyGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn


class AgentHierarchyGroup(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentHierarchyGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AgentHierarchyGroup:
    out: AgentHierarchyGroup = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
