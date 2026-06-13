"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandCapacityReservationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.on_demand_capacity_reservation_preference
    import aws_sdk_emr.types.on_demand_capacity_reservation_usage_strategy
    import aws_sdk_emr.types.xml_string_max_len256


class OnDemandCapacityReservationOptions(TypedDict):
    usage_strategy: NotRequired[
        "aws_sdk_emr.types.on_demand_capacity_reservation_usage_strategy.OnDemandCapacityReservationUsageStrategy"
    ]
    """<p>Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.</p> <p>If you specify <code>use-capacity-reservations-first</code>, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (<code>lowest-price</code>) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (<code>lowest-price</code>).</p> <p>If you do not specify a value, the fleet fulfills the On-Demand capacity according to the chosen On-Demand allocation strategy.</p>"""
    capacity_reservation_preference: NotRequired[
        "aws_sdk_emr.types.on_demand_capacity_reservation_preference.OnDemandCapacityReservationPreference"
    ]
    """<p>Indicates the instance's Capacity Reservation preferences. Possible preferences include:</p> <ul> <li> <p> <code>open</code> - The instance can run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).</p> </li> <li> <p> <code>none</code> - The instance avoids running in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance.</p> </li> </ul>"""
    capacity_reservation_resource_group_arn: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The ARN of the Capacity Reservation resource group in which to run the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDemandCapacityReservationOptions) -> dict:
    out: dict = {}
    if "usage_strategy" in value:
        import aws_sdk_emr.types.on_demand_capacity_reservation_usage_strategy

        out["UsageStrategy"] = (
            aws_sdk_emr.types.on_demand_capacity_reservation_usage_strategy.serialize_aws_json_1_1(
                value["usage_strategy"]
            )
        )
    if "capacity_reservation_preference" in value:
        import aws_sdk_emr.types.on_demand_capacity_reservation_preference

        out["CapacityReservationPreference"] = (
            aws_sdk_emr.types.on_demand_capacity_reservation_preference.serialize_aws_json_1_1(
                value["capacity_reservation_preference"]
            )
        )
    if "capacity_reservation_resource_group_arn" in value:
        out["CapacityReservationResourceGroupArn"] = value[
            "capacity_reservation_resource_group_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> OnDemandCapacityReservationOptions:
    out: OnDemandCapacityReservationOptions = {}  # type: ignore[typeddict-item]
    if "UsageStrategy" in data:
        import aws_sdk_emr.types.on_demand_capacity_reservation_usage_strategy

        out["usage_strategy"] = (
            aws_sdk_emr.types.on_demand_capacity_reservation_usage_strategy.deserialize_aws_json_1_1(
                data["UsageStrategy"]
            )
        )
    if "CapacityReservationPreference" in data:
        import aws_sdk_emr.types.on_demand_capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            aws_sdk_emr.types.on_demand_capacity_reservation_preference.deserialize_aws_json_1_1(
                data["CapacityReservationPreference"]
            )
        )
    if "CapacityReservationResourceGroupArn" in data:
        out["capacity_reservation_resource_group_arn"] = data[
            "CapacityReservationResourceGroupArn"
        ]
    return out
