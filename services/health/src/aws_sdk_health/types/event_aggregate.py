"""Generated from Smithy shape ``com.amazonaws.health#EventAggregate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.aggregate_value
    import aws_sdk_health.types.count


class EventAggregate(TypedDict, closed=True):
    aggregate_value: NotRequired["aws_sdk_health.types.aggregate_value.aggregateValue"]
    """<p>The issue type for the associated count.</p>"""
    count: "aws_sdk_health.types.count.count"
    """<p>The number of events of the associated issue type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventAggregate) -> dict:
    out: dict = {}
    if "aggregate_value" in value:
        out["aggregateValue"] = value["aggregate_value"]
    out["count"] = value.get("count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> EventAggregate:
    out: EventAggregate = {}  # type: ignore[typeddict-item]
    if "aggregateValue" in data:
        out["aggregate_value"] = data["aggregateValue"]
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
