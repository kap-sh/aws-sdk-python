"""Generated from Smithy shape ``com.amazonaws.location#ListGeofenceCollectionsResponseEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class ListGeofenceCollectionsResponseEntry(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection.</p>"""
    description: "aws_sdk_location.types.resource_description.ResourceDescription"
    """<p>The description for the geofence collection</p>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. Always returns <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>No longer used. Always returns an empty string.</p>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the geofence collection was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>Specifies a timestamp for when the resource was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGeofenceCollectionsResponseEntry) -> dict:
    out: dict = {}
    out["CollectionName"] = value["collection_name"]
    out["Description"] = value["description"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ListGeofenceCollectionsResponseEntry:
    out: ListGeofenceCollectionsResponseEntry = {}  # type: ignore[typeddict-item]
    if "CollectionName" in data:
        out["collection_name"] = data["CollectionName"]
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.collection_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.description required"
        )
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "PricingPlanDataSource" in data:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.create_time required"
        )
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.update_time required"
        )
    return out
