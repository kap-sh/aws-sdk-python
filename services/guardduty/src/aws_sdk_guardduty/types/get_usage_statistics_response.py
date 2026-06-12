"""Generated from Smithy shape ``com.amazonaws.guardduty#GetUsageStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.usage_statistics


class GetUsageStatisticsResponse(TypedDict):
    usage_statistics: NotRequired[
        "aws_sdk_guardduty.types.usage_statistics.UsageStatistics"
    ]
    """<p>The usage statistics object. If a UsageStatisticType was provided, the objects representing other types will be null.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageStatisticsResponse) -> dict:
    out: dict = {}
    if "usage_statistics" in value:
        import aws_sdk_guardduty.types.usage_statistics

        out["usageStatistics"] = (
            aws_sdk_guardduty.types.usage_statistics.serialize_json(
                value["usage_statistics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetUsageStatisticsResponse:
    out: GetUsageStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "usageStatistics" in data:
        import aws_sdk_guardduty.types.usage_statistics

        out["usage_statistics"] = (
            aws_sdk_guardduty.types.usage_statistics.deserialize_json(
                data["usageStatistics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
