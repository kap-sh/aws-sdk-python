"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Conditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.object_count
    import capo_customer_profiles.types.range
    import capo_customer_profiles.types.threshold


class Conditions(TypedDict, closed=True):
    range: NotRequired["capo_customer_profiles.types.range.Range"]
    """<p>The relative time period over which data is included in the aggregation.</p>"""
    object_count: NotRequired["capo_customer_profiles.types.object_count.ObjectCount"]
    """<p>The number of profile objects used for the calculated attribute.</p>"""
    threshold: NotRequired["capo_customer_profiles.types.threshold.Threshold"]
    """<p>The threshold for the calculated attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Conditions) -> dict:
    out: dict = {}
    if "range" in value:
        import capo_customer_profiles.types.range

        out["Range"] = capo_customer_profiles.types.range.serialize_json(value["range"])
    if "object_count" in value:
        out["ObjectCount"] = value["object_count"]
    if "threshold" in value:
        import capo_customer_profiles.types.threshold

        out["Threshold"] = capo_customer_profiles.types.threshold.serialize_json(
            value["threshold"]
        )
    return out


def deserialize_json(data: dict) -> Conditions:
    out: Conditions = {}  # type: ignore[typeddict-item]
    if "Range" in data:
        import capo_customer_profiles.types.range

        out["range"] = capo_customer_profiles.types.range.deserialize_json(
            data["Range"]
        )
    if "ObjectCount" in data:
        out["object_count"] = data["ObjectCount"]
    if "Threshold" in data:
        import capo_customer_profiles.types.threshold

        out["threshold"] = capo_customer_profiles.types.threshold.deserialize_json(
            data["Threshold"]
        )
    return out
