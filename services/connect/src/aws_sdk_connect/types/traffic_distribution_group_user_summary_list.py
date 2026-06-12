"""Generated from Smithy shape ``com.amazonaws.connect#TrafficDistributionGroupUserSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.traffic_distribution_group_user_summary

TrafficDistributionGroupUserSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.traffic_distribution_group_user_summary.TrafficDistributionGroupUserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficDistributionGroupUserSummaryList) -> list:
    import aws_sdk_connect.types.traffic_distribution_group_user_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.traffic_distribution_group_user_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TrafficDistributionGroupUserSummaryList:
    import aws_sdk_connect.types.traffic_distribution_group_user_summary

    out: TrafficDistributionGroupUserSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.traffic_distribution_group_user_summary.deserialize_json(
                item
            )
        )
    return out
