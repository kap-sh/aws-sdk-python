"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedEventResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendation_related_event_resource_name
    import capo_devops_guru.types.recommendation_related_event_resource_type


class RecommendationRelatedEventResource(TypedDict, closed=True):
    name: NotRequired[
        "capo_devops_guru.types.recommendation_related_event_resource_name.RecommendationRelatedEventResourceName"
    ]
    """<p> The name of the resource that emitted the event. This corresponds to the <code>Name</code> field in an <code>EventResource</code> object. </p>"""
    type: NotRequired[
        "capo_devops_guru.types.recommendation_related_event_resource_type.RecommendationRelatedEventResourceType"
    ]
    """<p> The type of the resource that emitted the event. This corresponds to the <code>Type</code> field in an <code>EventResource</code> object. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedEventResource) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> RecommendationRelatedEventResource:
    out: RecommendationRelatedEventResource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
