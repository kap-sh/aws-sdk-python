"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_arns_list
    import aws_sdk_quicksight.types.day_of_the_week
    import aws_sdk_quicksight.types.q_business_insights_status
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.visual_custom_action_defaults


class AssetOptions(TypedDict):
    timezone: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>Determines the timezone for the analysis.</p>"""
    week_start: NotRequired["aws_sdk_quicksight.types.day_of_the_week.DayOfTheWeek"]
    """<p>Determines the week start day for an analysis.</p>"""
    q_business_insights_status: NotRequired[
        "aws_sdk_quicksight.types.q_business_insights_status.QBusinessInsightsStatus"
    ]
    """<p>Determines whether insight summaries from Amazon Q Business are allowed in Dashboard Q&A.</p>"""
    excluded_data_set_arns: NotRequired[
        "aws_sdk_quicksight.types.data_set_arns_list.DataSetArnsList"
    ]
    """<p>A list of dataset ARNS to exclude from Dashboard Q&A.</p>"""
    custom_action_defaults: NotRequired[
        "aws_sdk_quicksight.types.visual_custom_action_defaults.VisualCustomActionDefaults"
    ]
    """<p>A list of visual custom actions for the analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetOptions) -> dict:
    out: dict = {}
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "week_start" in value:
        import aws_sdk_quicksight.types.day_of_the_week

        out["WeekStart"] = aws_sdk_quicksight.types.day_of_the_week.serialize_json(
            value["week_start"]
        )
    if "q_business_insights_status" in value:
        import aws_sdk_quicksight.types.q_business_insights_status

        out["QBusinessInsightsStatus"] = (
            aws_sdk_quicksight.types.q_business_insights_status.serialize_json(
                value["q_business_insights_status"]
            )
        )
    if "excluded_data_set_arns" in value:
        import aws_sdk_quicksight.types.data_set_arns_list

        out["ExcludedDataSetArns"] = (
            aws_sdk_quicksight.types.data_set_arns_list.serialize_json(
                value["excluded_data_set_arns"]
            )
        )
    if "custom_action_defaults" in value:
        import aws_sdk_quicksight.types.visual_custom_action_defaults

        out["CustomActionDefaults"] = (
            aws_sdk_quicksight.types.visual_custom_action_defaults.serialize_json(
                value["custom_action_defaults"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetOptions:
    out: AssetOptions = {}  # type: ignore[typeddict-item]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "WeekStart" in data:
        import aws_sdk_quicksight.types.day_of_the_week

        out["week_start"] = aws_sdk_quicksight.types.day_of_the_week.deserialize_json(
            data["WeekStart"]
        )
    if "QBusinessInsightsStatus" in data:
        import aws_sdk_quicksight.types.q_business_insights_status

        out["q_business_insights_status"] = (
            aws_sdk_quicksight.types.q_business_insights_status.deserialize_json(
                data["QBusinessInsightsStatus"]
            )
        )
    if "ExcludedDataSetArns" in data:
        import aws_sdk_quicksight.types.data_set_arns_list

        out["excluded_data_set_arns"] = (
            aws_sdk_quicksight.types.data_set_arns_list.deserialize_json(
                data["ExcludedDataSetArns"]
            )
        )
    if "CustomActionDefaults" in data:
        import aws_sdk_quicksight.types.visual_custom_action_defaults

        out["custom_action_defaults"] = (
            aws_sdk_quicksight.types.visual_custom_action_defaults.deserialize_json(
                data["CustomActionDefaults"]
            )
        )
    return out
