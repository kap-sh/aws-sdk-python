"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIConditionalFormattingOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.kpi_actual_value_conditional_formatting
    import aws_sdk_quicksight.types.kpi_comparison_value_conditional_formatting
    import aws_sdk_quicksight.types.kpi_primary_value_conditional_formatting
    import aws_sdk_quicksight.types.kpi_progress_bar_conditional_formatting


class KPIConditionalFormattingOption(TypedDict):
    primary_value: NotRequired[
        "aws_sdk_quicksight.types.kpi_primary_value_conditional_formatting.KPIPrimaryValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the primary value of a KPI visual.</p>"""
    progress_bar: NotRequired[
        "aws_sdk_quicksight.types.kpi_progress_bar_conditional_formatting.KPIProgressBarConditionalFormatting"
    ]
    """<p>The conditional formatting for the progress bar of a KPI visual.</p>"""
    actual_value: NotRequired[
        "aws_sdk_quicksight.types.kpi_actual_value_conditional_formatting.KPIActualValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the actual value of a KPI visual.</p>"""
    comparison_value: NotRequired[
        "aws_sdk_quicksight.types.kpi_comparison_value_conditional_formatting.KPIComparisonValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the comparison value of a KPI visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIConditionalFormattingOption) -> dict:
    out: dict = {}
    if "primary_value" in value:
        import aws_sdk_quicksight.types.kpi_primary_value_conditional_formatting

        out["PrimaryValue"] = (
            aws_sdk_quicksight.types.kpi_primary_value_conditional_formatting.serialize_json(
                value["primary_value"]
            )
        )
    if "progress_bar" in value:
        import aws_sdk_quicksight.types.kpi_progress_bar_conditional_formatting

        out["ProgressBar"] = (
            aws_sdk_quicksight.types.kpi_progress_bar_conditional_formatting.serialize_json(
                value["progress_bar"]
            )
        )
    if "actual_value" in value:
        import aws_sdk_quicksight.types.kpi_actual_value_conditional_formatting

        out["ActualValue"] = (
            aws_sdk_quicksight.types.kpi_actual_value_conditional_formatting.serialize_json(
                value["actual_value"]
            )
        )
    if "comparison_value" in value:
        import aws_sdk_quicksight.types.kpi_comparison_value_conditional_formatting

        out["ComparisonValue"] = (
            aws_sdk_quicksight.types.kpi_comparison_value_conditional_formatting.serialize_json(
                value["comparison_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIConditionalFormattingOption:
    out: KPIConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if "PrimaryValue" in data:
        import aws_sdk_quicksight.types.kpi_primary_value_conditional_formatting

        out["primary_value"] = (
            aws_sdk_quicksight.types.kpi_primary_value_conditional_formatting.deserialize_json(
                data["PrimaryValue"]
            )
        )
    if "ProgressBar" in data:
        import aws_sdk_quicksight.types.kpi_progress_bar_conditional_formatting

        out["progress_bar"] = (
            aws_sdk_quicksight.types.kpi_progress_bar_conditional_formatting.deserialize_json(
                data["ProgressBar"]
            )
        )
    if "ActualValue" in data:
        import aws_sdk_quicksight.types.kpi_actual_value_conditional_formatting

        out["actual_value"] = (
            aws_sdk_quicksight.types.kpi_actual_value_conditional_formatting.deserialize_json(
                data["ActualValue"]
            )
        )
    if "ComparisonValue" in data:
        import aws_sdk_quicksight.types.kpi_comparison_value_conditional_formatting

        out["comparison_value"] = (
            aws_sdk_quicksight.types.kpi_comparison_value_conditional_formatting.deserialize_json(
                data["ComparisonValue"]
            )
        )
    return out
