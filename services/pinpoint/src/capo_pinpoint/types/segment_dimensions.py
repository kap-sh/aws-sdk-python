"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentDimensions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.map_of_attribute_dimension
    import capo_pinpoint.types.map_of_metric_dimension
    import capo_pinpoint.types.segment_behaviors
    import capo_pinpoint.types.segment_demographics
    import capo_pinpoint.types.segment_location


class SegmentDimensions(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_pinpoint.types.map_of_attribute_dimension.MapOfAttributeDimension"
    ]
    """<p>One or more custom attributes to use as criteria for the segment.</p>"""
    behavior: NotRequired["capo_pinpoint.types.segment_behaviors.SegmentBehaviors"]
    """<p>The behavior-based criteria, such as how recently users have used your app, for the segment.</p>"""
    demographic: NotRequired[
        "capo_pinpoint.types.segment_demographics.SegmentDemographics"
    ]
    """<p>The demographic-based criteria, such as device platform, for the segment.</p>"""
    location: NotRequired["capo_pinpoint.types.segment_location.SegmentLocation"]
    """<p>The location-based criteria, such as region or GPS coordinates, for the segment.</p>"""
    metrics: NotRequired[
        "capo_pinpoint.types.map_of_metric_dimension.MapOfMetricDimension"
    ]
    """<p>One or more custom metrics to use as criteria for the segment.</p>"""
    user_attributes: NotRequired[
        "capo_pinpoint.types.map_of_attribute_dimension.MapOfAttributeDimension"
    ]
    """<p>One or more custom user attributes to use as criteria for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentDimensions) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_pinpoint.types.map_of_attribute_dimension

        out["Attributes"] = (
            capo_pinpoint.types.map_of_attribute_dimension.serialize_json(
                value["attributes"]
            )
        )
    if "behavior" in value:
        import capo_pinpoint.types.segment_behaviors

        out["Behavior"] = capo_pinpoint.types.segment_behaviors.serialize_json(
            value["behavior"]
        )
    if "demographic" in value:
        import capo_pinpoint.types.segment_demographics

        out["Demographic"] = capo_pinpoint.types.segment_demographics.serialize_json(
            value["demographic"]
        )
    if "location" in value:
        import capo_pinpoint.types.segment_location

        out["Location"] = capo_pinpoint.types.segment_location.serialize_json(
            value["location"]
        )
    if "metrics" in value:
        import capo_pinpoint.types.map_of_metric_dimension

        out["Metrics"] = capo_pinpoint.types.map_of_metric_dimension.serialize_json(
            value["metrics"]
        )
    if "user_attributes" in value:
        import capo_pinpoint.types.map_of_attribute_dimension

        out["UserAttributes"] = (
            capo_pinpoint.types.map_of_attribute_dimension.serialize_json(
                value["user_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> SegmentDimensions:
    out: SegmentDimensions = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import capo_pinpoint.types.map_of_attribute_dimension

        out["attributes"] = (
            capo_pinpoint.types.map_of_attribute_dimension.deserialize_json(
                data["Attributes"]
            )
        )
    if "Behavior" in data:
        import capo_pinpoint.types.segment_behaviors

        out["behavior"] = capo_pinpoint.types.segment_behaviors.deserialize_json(
            data["Behavior"]
        )
    if "Demographic" in data:
        import capo_pinpoint.types.segment_demographics

        out["demographic"] = capo_pinpoint.types.segment_demographics.deserialize_json(
            data["Demographic"]
        )
    if "Location" in data:
        import capo_pinpoint.types.segment_location

        out["location"] = capo_pinpoint.types.segment_location.deserialize_json(
            data["Location"]
        )
    if "Metrics" in data:
        import capo_pinpoint.types.map_of_metric_dimension

        out["metrics"] = capo_pinpoint.types.map_of_metric_dimension.deserialize_json(
            data["Metrics"]
        )
    if "UserAttributes" in data:
        import capo_pinpoint.types.map_of_attribute_dimension

        out["user_attributes"] = (
            capo_pinpoint.types.map_of_attribute_dimension.deserialize_json(
                data["UserAttributes"]
            )
        )
    return out
