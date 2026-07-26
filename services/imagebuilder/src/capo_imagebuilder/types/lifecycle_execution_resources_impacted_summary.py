"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourcesImpactedSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean


class LifecycleExecutionResourcesImpactedSummary(TypedDict, closed=True):
    has_impacted_resources: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Indicates whether an image resource that was identified for a lifecycle action has associated resources that are also impacted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionResourcesImpactedSummary) -> dict:
    out: dict = {}
    out["hasImpactedResources"] = value.get("has_impacted_resources", False)
    return out


def deserialize_json(data: dict) -> LifecycleExecutionResourcesImpactedSummary:
    out: LifecycleExecutionResourcesImpactedSummary = {}  # type: ignore[typeddict-item]
    if "hasImpactedResources" in data:
        out["has_impacted_resources"] = data["hasImpactedResources"]
    else:
        out["has_impacted_resources"] = False
    return out
