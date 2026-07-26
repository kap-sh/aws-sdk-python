"""Generated from Smithy shape ``com.amazonaws.location#UpdateGeofenceCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name


class UpdateGeofenceCollectionRequest(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection to update.</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>This parameter is no longer used.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>Updates the description for the geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGeofenceCollectionRequest) -> dict:
    out: dict = {}
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateGeofenceCollectionRequest:
    out: UpdateGeofenceCollectionRequest = {}  # type: ignore[typeddict-item]
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "PricingPlanDataSource" in data:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
