"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationUtilizationGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.attributes
    import aws_sdk_cost_explorer.types.reservation_aggregates
    import aws_sdk_cost_explorer.types.reservation_group_key
    import aws_sdk_cost_explorer.types.reservation_group_value


class ReservationUtilizationGroup(TypedDict):
    key: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_group_key.ReservationGroupKey"
    ]
    """<p>The key for a specific reservation attribute.</p>"""
    value: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_group_value.ReservationGroupValue"
    ]
    """<p>The value of a specific reservation attribute.</p>"""
    attributes: NotRequired["aws_sdk_cost_explorer.types.attributes.Attributes"]
    """<p>The attributes for this group of reservations.</p>"""
    utilization: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_aggregates.ReservationAggregates"
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
        import aws_sdk_cost_explorer.types.attributes

        out["Attributes"] = (
            aws_sdk_cost_explorer.types.attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "utilization" in value:
        import aws_sdk_cost_explorer.types.reservation_aggregates

        out["Utilization"] = (
            aws_sdk_cost_explorer.types.reservation_aggregates.serialize_aws_json_1_1(
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
        import aws_sdk_cost_explorer.types.attributes

        out["attributes"] = (
            aws_sdk_cost_explorer.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Utilization" in data:
        import aws_sdk_cost_explorer.types.reservation_aggregates

        out["utilization"] = (
            aws_sdk_cost_explorer.types.reservation_aggregates.deserialize_aws_json_1_1(
                data["Utilization"]
            )
        )
    return out
