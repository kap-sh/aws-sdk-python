"""Generated from Smithy shape ``com.amazonaws.eks#ControlPlanePlacementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class ControlPlanePlacementRequest(TypedDict, closed=True):
    group_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the placement group for the Kubernetes control plane instances. This setting can't be changed after cluster creation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlanePlacementRequest) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    return out


def deserialize_json(data: dict) -> ControlPlanePlacementRequest:
    out: ControlPlanePlacementRequest = {}  # type: ignore[typeddict-item]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    return out
