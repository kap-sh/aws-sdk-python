"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DashboardSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.dashboard_summary

DashboardSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.dashboard_summary.DashboardSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardSummaries) -> list:
    import aws_sdk_iotsitewise.types.dashboard_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.dashboard_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashboardSummaries:
    import aws_sdk_iotsitewise.types.dashboard_summary

    out: DashboardSummaries = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.dashboard_summary.deserialize_json(item))
    return out
