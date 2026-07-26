"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationUtilizationGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.reservation_utilization_group

ReservationUtilizationGroups: TypeAlias = list[
    "capo_cost_explorer.types.reservation_utilization_group.ReservationUtilizationGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationUtilizationGroups) -> list:
    import capo_cost_explorer.types.reservation_utilization_group

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.reservation_utilization_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservationUtilizationGroups:
    import capo_cost_explorer.types.reservation_utilization_group

    out: ReservationUtilizationGroups = []
    for item in data:
        out.append(
            capo_cost_explorer.types.reservation_utilization_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
