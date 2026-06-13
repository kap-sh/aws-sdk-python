"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIR``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_ir_contribution_analysis
    import aws_sdk_quicksight.types.topic_ir_filter_list
    import aws_sdk_quicksight.types.topic_ir_group_by_list
    import aws_sdk_quicksight.types.topic_ir_metric_list
    import aws_sdk_quicksight.types.topic_sort_clause
    import aws_sdk_quicksight.types.visual_options


class TopicIR(TypedDict):
    metrics: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_metric_list.TopicIRMetricList"
    ]
    """<p>The metrics for the <code>TopicIR</code>.</p>"""
    group_by_list: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_group_by_list.TopicIRGroupByList"
    ]
    """<p>The GroupBy list for the <code>TopicIR</code>.</p>"""
    filters: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_filter_list.TopicIRFilterList"
    ]
    """<p>The filters for the <code>TopicIR</code>.</p>"""
    sort: NotRequired["aws_sdk_quicksight.types.topic_sort_clause.TopicSortClause"]
    """<p>The sort for the <code>TopicIR</code>.</p>"""
    contribution_analysis: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_contribution_analysis.TopicIRContributionAnalysis"
    ]
    """<p>The contribution analysis for the <code>TopicIR</code>.</p>"""
    visual: NotRequired["aws_sdk_quicksight.types.visual_options.VisualOptions"]
    """<p>The visual for the <code>TopicIR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIR) -> dict:
    out: dict = {}
    if "metrics" in value:
        import aws_sdk_quicksight.types.topic_ir_metric_list

        out["Metrics"] = aws_sdk_quicksight.types.topic_ir_metric_list.serialize_json(
            value["metrics"]
        )
    if "group_by_list" in value:
        import aws_sdk_quicksight.types.topic_ir_group_by_list

        out["GroupByList"] = (
            aws_sdk_quicksight.types.topic_ir_group_by_list.serialize_json(
                value["group_by_list"]
            )
        )
    if "filters" in value:
        import aws_sdk_quicksight.types.topic_ir_filter_list

        out["Filters"] = aws_sdk_quicksight.types.topic_ir_filter_list.serialize_json(
            value["filters"]
        )
    if "sort" in value:
        import aws_sdk_quicksight.types.topic_sort_clause

        out["Sort"] = aws_sdk_quicksight.types.topic_sort_clause.serialize_json(
            value["sort"]
        )
    if "contribution_analysis" in value:
        import aws_sdk_quicksight.types.topic_ir_contribution_analysis

        out["ContributionAnalysis"] = (
            aws_sdk_quicksight.types.topic_ir_contribution_analysis.serialize_json(
                value["contribution_analysis"]
            )
        )
    if "visual" in value:
        import aws_sdk_quicksight.types.visual_options

        out["Visual"] = aws_sdk_quicksight.types.visual_options.serialize_json(
            value["visual"]
        )
    return out


def deserialize_json(data: dict) -> TopicIR:
    out: TopicIR = {}  # type: ignore[typeddict-item]
    if "Metrics" in data:
        import aws_sdk_quicksight.types.topic_ir_metric_list

        out["metrics"] = aws_sdk_quicksight.types.topic_ir_metric_list.deserialize_json(
            data["Metrics"]
        )
    if "GroupByList" in data:
        import aws_sdk_quicksight.types.topic_ir_group_by_list

        out["group_by_list"] = (
            aws_sdk_quicksight.types.topic_ir_group_by_list.deserialize_json(
                data["GroupByList"]
            )
        )
    if "Filters" in data:
        import aws_sdk_quicksight.types.topic_ir_filter_list

        out["filters"] = aws_sdk_quicksight.types.topic_ir_filter_list.deserialize_json(
            data["Filters"]
        )
    if "Sort" in data:
        import aws_sdk_quicksight.types.topic_sort_clause

        out["sort"] = aws_sdk_quicksight.types.topic_sort_clause.deserialize_json(
            data["Sort"]
        )
    if "ContributionAnalysis" in data:
        import aws_sdk_quicksight.types.topic_ir_contribution_analysis

        out["contribution_analysis"] = (
            aws_sdk_quicksight.types.topic_ir_contribution_analysis.deserialize_json(
                data["ContributionAnalysis"]
            )
        )
    if "Visual" in data:
        import aws_sdk_quicksight.types.visual_options

        out["visual"] = aws_sdk_quicksight.types.visual_options.deserialize_json(
            data["Visual"]
        )
    return out
