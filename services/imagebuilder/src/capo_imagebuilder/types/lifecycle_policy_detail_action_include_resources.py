"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailActionIncludeResources``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean


class LifecyclePolicyDetailActionIncludeResources(TypedDict, closed=True):
    amis: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Specifies whether the lifecycle action should apply to distributed AMIs.</p>"""
    snapshots: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Specifies whether the lifecycle action should apply to snapshots associated with distributed AMIs.</p>"""
    containers: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Specifies whether the lifecycle action should apply to distributed containers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailActionIncludeResources) -> dict:
    out: dict = {}
    out["amis"] = value.get("amis", False)
    out["snapshots"] = value.get("snapshots", False)
    out["containers"] = value.get("containers", False)
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailActionIncludeResources:
    out: LifecyclePolicyDetailActionIncludeResources = {}  # type: ignore[typeddict-item]
    if "amis" in data:
        out["amis"] = data["amis"]
    else:
        out["amis"] = False
    if "snapshots" in data:
        out["snapshots"] = data["snapshots"]
    else:
        out["snapshots"] = False
    if "containers" in data:
        out["containers"] = data["containers"]
    else:
        out["containers"] = False
    return out
