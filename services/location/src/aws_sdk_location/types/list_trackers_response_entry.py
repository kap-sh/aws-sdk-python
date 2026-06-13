"""Generated from Smithy shape ``com.amazonaws.location#ListTrackersResponseEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class ListTrackersResponseEntry(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource.</p>"""
    description: "aws_sdk_location.types.resource_description.ResourceDescription"
    """<p>The description for the tracker resource.</p>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>Always returns <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>No longer used. Always returns an empty string.</p>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the tracker resource was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp at which the device's position was determined. Uses <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrackersResponseEntry) -> dict:
    out: dict = {}
    out["TrackerName"] = value["tracker_name"]
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


def deserialize_json(data: dict) -> ListTrackersResponseEntry:
    out: ListTrackersResponseEntry = {}  # type: ignore[typeddict-item]
    if "TrackerName" in data:
        out["tracker_name"] = data["TrackerName"]
    else:
        raise DeserializationError("ListTrackersResponseEntry.tracker_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("ListTrackersResponseEntry.description required")
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
        raise DeserializationError("ListTrackersResponseEntry.create_time required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("ListTrackersResponseEntry.update_time required")
    return out
