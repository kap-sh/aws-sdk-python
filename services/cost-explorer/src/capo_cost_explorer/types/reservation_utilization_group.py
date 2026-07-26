"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationUtilizationGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.attributes
    import capo_cost_explorer.types.reservation_aggregates
    import capo_cost_explorer.types.reservation_group_key
    import capo_cost_explorer.types.reservation_group_value


class ReservationUtilizationGroup(TypedDict, closed=True):
    key: NotRequired[
        "capo_cost_explorer.types.reservation_group_key.ReservationGroupKey"
    ]
    """<p>The key for a specific reservation attribute.</p>"""
    value: NotRequired[
        "capo_cost_explorer.types.reservation_group_value.ReservationGroupValue"
    ]
    """<p>The value of a specific reservation attribute.</p>"""
    attributes: NotRequired["capo_cost_explorer.types.attributes.Attributes"]
    """<p>The attributes for this group of reservations.</p>"""
    utilization: NotRequired[
        "capo_cost_explorer.types.reservation_aggregates.ReservationAggregates"
    ]
    """<p>How much you used this group of reservations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationUtilizationGroup) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "attributes" in value:
        import capo_cost_explorer.types.attributes

        out["Attributes"] = capo_cost_explorer.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    if "utilization" in value:
        import capo_cost_explorer.types.reservation_aggregates

        out["Utilization"] = (
            capo_cost_explorer.types.reservation_aggregates.serialize_aws_json_1_1(
                value["utilization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationUtilizationGroup:
    out: ReservationUtilizationGroup = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Attributes" in data:
        import capo_cost_explorer.types.attributes

        out["attributes"] = (
            capo_cost_explorer.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Utilization" in data:
        import capo_cost_explorer.types.reservation_aggregates

        out["utilization"] = (
            capo_cost_explorer.types.reservation_aggregates.deserialize_aws_json_1_1(
                data["Utilization"]
            )
        )
    return out
