"""Generated from Smithy shape ``com.amazonaws.quicksight#AmazonQInQuickSightDashboardConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.executive_summary_configurations


class AmazonQInQuickSightDashboardConfigurations(TypedDict, closed=True):
    executive_summary: NotRequired[
        "aws_sdk_quicksight.types.executive_summary_configurations.ExecutiveSummaryConfigurations"
    ]
    """<p>A generated executive summary of an embedded Quick Sight dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonQInQuickSightDashboardConfigurations) -> dict:
    out: dict = {}
    if "executive_summary" in value:
        import aws_sdk_quicksight.types.executive_summary_configurations

        out["ExecutiveSummary"] = (
            aws_sdk_quicksight.types.executive_summary_configurations.serialize_json(
                value["executive_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonQInQuickSightDashboardConfigurations:
    out: AmazonQInQuickSightDashboardConfigurations = {}  # type: ignore[typeddict-item]
    if "ExecutiveSummary" in data:
        import aws_sdk_quicksight.types.executive_summary_configurations

        out["executive_summary"] = (
            aws_sdk_quicksight.types.executive_summary_configurations.deserialize_json(
                data["ExecutiveSummary"]
            )
        )
    return out
