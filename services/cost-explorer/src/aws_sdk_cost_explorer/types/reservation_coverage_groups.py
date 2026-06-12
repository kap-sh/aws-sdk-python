"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationCoverageGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.reservation_coverage_group

ReservationCoverageGroups: TypeAlias = list[
    "aws_sdk_cost_explorer.types.reservation_coverage_group.ReservationCoverageGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationCoverageGroups) -> list:
    import aws_sdk_cost_explorer.types.reservation_coverage_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.reservation_coverage_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservationCoverageGroups:
    import aws_sdk_cost_explorer.types.reservation_coverage_group

    out: ReservationCoverageGroups = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.reservation_coverage_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
