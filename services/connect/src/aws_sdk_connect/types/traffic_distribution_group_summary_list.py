"""Generated from Smithy shape ``com.amazonaws.connect#TrafficDistributionGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.traffic_distribution_group_summary

TrafficDistributionGroupSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.traffic_distribution_group_summary.TrafficDistributionGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficDistributionGroupSummaryList) -> list:
    import aws_sdk_connect.types.traffic_distribution_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.traffic_distribution_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TrafficDistributionGroupSummaryList:
    import aws_sdk_connect.types.traffic_distribution_group_summary

    out: TrafficDistributionGroupSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.traffic_distribution_group_summary.deserialize_json(
                item
            )
        )
    return out
