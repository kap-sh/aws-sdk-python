"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardPublishOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.ad_hoc_filtering_option
    import capo_quicksight.types.dashboard_visual_publish_options
    import capo_quicksight.types.data_point_drill_up_down_option
    import capo_quicksight.types.data_point_menu_label_option
    import capo_quicksight.types.data_point_tooltip_option
    import capo_quicksight.types.data_qa_enabled_option
    import capo_quicksight.types.data_stories_sharing_option
    import capo_quicksight.types.executive_summary_option
    import capo_quicksight.types.export_to_csv_option
    import capo_quicksight.types.export_with_hidden_fields_option
    import capo_quicksight.types.quick_suite_actions_option
    import capo_quicksight.types.sheet_controls_option
    import capo_quicksight.types.sheet_layout_element_maximization_option
    import capo_quicksight.types.visual_axis_sort_option
    import capo_quicksight.types.visual_menu_option


class DashboardPublishOptions(TypedDict, closed=True):
    ad_hoc_filtering_option: NotRequired[
        "capo_quicksight.types.ad_hoc_filtering_option.AdHocFilteringOption"
    ]
    """<p>Ad hoc (one-time) filtering option.</p>"""
    export_to_csv_option: NotRequired[
        "capo_quicksight.types.export_to_csv_option.ExportToCSVOption"
    ]
    """<p>Export to .csv option.</p>"""
    sheet_controls_option: NotRequired[
        "capo_quicksight.types.sheet_controls_option.SheetControlsOption"
    ]
    """<p>Sheet controls option.</p>"""
    visual_publish_options: NotRequired[
        "capo_quicksight.types.dashboard_visual_publish_options.DashboardVisualPublishOptions"
    ]
    """<p>The visual publish options of a visual in a dashboard.</p>"""
    sheet_layout_element_maximization_option: NotRequired[
        "capo_quicksight.types.sheet_layout_element_maximization_option.SheetLayoutElementMaximizationOption"
    ]
    """<p>The sheet layout maximization options of a dashbaord.</p>"""
    visual_menu_option: NotRequired[
        "capo_quicksight.types.visual_menu_option.VisualMenuOption"
    ]
    """<p>The menu options of a visual in a dashboard.</p>"""
    visual_axis_sort_option: NotRequired[
        "capo_quicksight.types.visual_axis_sort_option.VisualAxisSortOption"
    ]
    """<p>The axis sort options of a dashboard.</p>"""
    export_with_hidden_fields_option: NotRequired[
        "capo_quicksight.types.export_with_hidden_fields_option.ExportWithHiddenFieldsOption"
    ]
    """<p>Determines if hidden fields are exported with a dashboard.</p>"""
    data_point_drill_up_down_option: NotRequired[
        "capo_quicksight.types.data_point_drill_up_down_option.DataPointDrillUpDownOption"
    ]
    """<p>The drill-down options of data points in a dashboard.</p>"""
    data_point_menu_label_option: NotRequired[
        "capo_quicksight.types.data_point_menu_label_option.DataPointMenuLabelOption"
    ]
    """<p>The data point menu label options of a dashboard.</p>"""
    data_point_tooltip_option: NotRequired[
        "capo_quicksight.types.data_point_tooltip_option.DataPointTooltipOption"
    ]
    """<p>The data point tool tip options of a dashboard.</p>"""
    data_qa_enabled_option: NotRequired[
        "capo_quicksight.types.data_qa_enabled_option.DataQAEnabledOption"
    ]
    """<p>Adds Q&A capabilities to an Quick Sight dashboard. If no topic is linked, Dashboard Q&A uses the data values that are rendered on the dashboard. End users can use Dashboard Q&A to ask for different slices of the data that they see on the dashboard. If a topic is linked, Topic Q&A is used.</p>"""
    quick_suite_actions_option: NotRequired[
        "capo_quicksight.types.quick_suite_actions_option.QuickSuiteActionsOption"
    ]
    """<p>Determines if Actions in Amazon Quick Suite are enabled in a dashboard.</p>"""
    executive_summary_option: NotRequired[
        "capo_quicksight.types.executive_summary_option.ExecutiveSummaryOption"
    ]
    """<p>Executive summary option.</p>"""
    data_stories_sharing_option: NotRequired[
        "capo_quicksight.types.data_stories_sharing_option.DataStoriesSharingOption"
    ]
    """<p>Data stories sharing option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardPublishOptions) -> dict:
    out: dict = {}
    if "ad_hoc_filtering_option" in value:
        import capo_quicksight.types.ad_hoc_filtering_option

        out["AdHocFilteringOption"] = (
            capo_quicksight.types.ad_hoc_filtering_option.serialize_json(
                value["ad_hoc_filtering_option"]
            )
        )
    if "export_to_csv_option" in value:
        import capo_quicksight.types.export_to_csv_option

        out["ExportToCSVOption"] = (
            capo_quicksight.types.export_to_csv_option.serialize_json(
                value["export_to_csv_option"]
            )
        )
    if "sheet_controls_option" in value:
        import capo_quicksight.types.sheet_controls_option

        out["SheetControlsOption"] = (
            capo_quicksight.types.sheet_controls_option.serialize_json(
                value["sheet_controls_option"]
            )
        )
    if "visual_publish_options" in value:
        import capo_quicksight.types.dashboard_visual_publish_options

        out["VisualPublishOptions"] = (
            capo_quicksight.types.dashboard_visual_publish_options.serialize_json(
                value["visual_publish_options"]
            )
        )
    if "sheet_layout_element_maximization_option" in value:
        import capo_quicksight.types.sheet_layout_element_maximization_option

        out["SheetLayoutElementMaximizationOption"] = (
            capo_quicksight.types.sheet_layout_element_maximization_option.serialize_json(
                value["sheet_layout_element_maximization_option"]
            )
        )
    if "visual_menu_option" in value:
        import capo_quicksight.types.visual_menu_option

        out["VisualMenuOption"] = (
            capo_quicksight.types.visual_menu_option.serialize_json(
                value["visual_menu_option"]
            )
        )
    if "visual_axis_sort_option" in value:
        import capo_quicksight.types.visual_axis_sort_option

        out["VisualAxisSortOption"] = (
            capo_quicksight.types.visual_axis_sort_option.serialize_json(
                value["visual_axis_sort_option"]
            )
        )
    if "export_with_hidden_fields_option" in value:
        import capo_quicksight.types.export_with_hidden_fields_option

        out["ExportWithHiddenFieldsOption"] = (
            capo_quicksight.types.export_with_hidden_fields_option.serialize_json(
                value["export_with_hidden_fields_option"]
            )
        )
    if "data_point_drill_up_down_option" in value:
        import capo_quicksight.types.data_point_drill_up_down_option

        out["DataPointDrillUpDownOption"] = (
            capo_quicksight.types.data_point_drill_up_down_option.serialize_json(
                value["data_point_drill_up_down_option"]
            )
        )
    if "data_point_menu_label_option" in value:
        import capo_quicksight.types.data_point_menu_label_option

        out["DataPointMenuLabelOption"] = (
            capo_quicksight.types.data_point_menu_label_option.serialize_json(
                value["data_point_menu_label_option"]
            )
        )
    if "data_point_tooltip_option" in value:
        import capo_quicksight.types.data_point_tooltip_option

        out["DataPointTooltipOption"] = (
            capo_quicksight.types.data_point_tooltip_option.serialize_json(
                value["data_point_tooltip_option"]
            )
        )
    if "data_qa_enabled_option" in value:
        import capo_quicksight.types.data_qa_enabled_option

        out["DataQAEnabledOption"] = (
            capo_quicksight.types.data_qa_enabled_option.serialize_json(
                value["data_qa_enabled_option"]
            )
        )
    if "quick_suite_actions_option" in value:
        import capo_quicksight.types.quick_suite_actions_option

        out["QuickSuiteActionsOption"] = (
            capo_quicksight.types.quick_suite_actions_option.serialize_json(
                value["quick_suite_actions_option"]
            )
        )
    if "executive_summary_option" in value:
        import capo_quicksight.types.executive_summary_option

        out["ExecutiveSummaryOption"] = (
            capo_quicksight.types.executive_summary_option.serialize_json(
                value["executive_summary_option"]
            )
        )
    if "data_stories_sharing_option" in value:
        import capo_quicksight.types.data_stories_sharing_option

        out["DataStoriesSharingOption"] = (
            capo_quicksight.types.data_stories_sharing_option.serialize_json(
                value["data_stories_sharing_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashboardPublishOptions:
    out: DashboardPublishOptions = {}  # type: ignore[typeddict-item]
    if "AdHocFilteringOption" in data:
        import capo_quicksight.types.ad_hoc_filtering_option

        out["ad_hoc_filtering_option"] = (
            capo_quicksight.types.ad_hoc_filtering_option.deserialize_json(
                data["AdHocFilteringOption"]
            )
        )
    if "ExportToCSVOption" in data:
        import capo_quicksight.types.export_to_csv_option

        out["export_to_csv_option"] = (
            capo_quicksight.types.export_to_csv_option.deserialize_json(
                data["ExportToCSVOption"]
            )
        )
    if "SheetControlsOption" in data:
        import capo_quicksight.types.sheet_controls_option

        out["sheet_controls_option"] = (
            capo_quicksight.types.sheet_controls_option.deserialize_json(
                data["SheetControlsOption"]
            )
        )
    if "VisualPublishOptions" in data:
        import capo_quicksight.types.dashboard_visual_publish_options

        out["visual_publish_options"] = (
            capo_quicksight.types.dashboard_visual_publish_options.deserialize_json(
                data["VisualPublishOptions"]
            )
        )
    if "SheetLayoutElementMaximizationOption" in data:
        import capo_quicksight.types.sheet_layout_element_maximization_option

        out["sheet_layout_element_maximization_option"] = (
            capo_quicksight.types.sheet_layout_element_maximization_option.deserialize_json(
                data["SheetLayoutElementMaximizationOption"]
            )
        )
    if "VisualMenuOption" in data:
        import capo_quicksight.types.visual_menu_option

        out["visual_menu_option"] = (
            capo_quicksight.types.visual_menu_option.deserialize_json(
                data["VisualMenuOption"]
            )
        )
    if "VisualAxisSortOption" in data:
        import capo_quicksight.types.visual_axis_sort_option

        out["visual_axis_sort_option"] = (
            capo_quicksight.types.visual_axis_sort_option.deserialize_json(
                data["VisualAxisSortOption"]
            )
        )
    if "ExportWithHiddenFieldsOption" in data:
        import capo_quicksight.types.export_with_hidden_fields_option

        out["export_with_hidden_fields_option"] = (
            capo_quicksight.types.export_with_hidden_fields_option.deserialize_json(
                data["ExportWithHiddenFieldsOption"]
            )
        )
    if "DataPointDrillUpDownOption" in data:
        import capo_quicksight.types.data_point_drill_up_down_option

        out["data_point_drill_up_down_option"] = (
            capo_quicksight.types.data_point_drill_up_down_option.deserialize_json(
                data["DataPointDrillUpDownOption"]
            )
        )
    if "DataPointMenuLabelOption" in data:
        import capo_quicksight.types.data_point_menu_label_option

        out["data_point_menu_label_option"] = (
            capo_quicksight.types.data_point_menu_label_option.deserialize_json(
                data["DataPointMenuLabelOption"]
            )
        )
    if "DataPointTooltipOption" in data:
        import capo_quicksight.types.data_point_tooltip_option

        out["data_point_tooltip_option"] = (
            capo_quicksight.types.data_point_tooltip_option.deserialize_json(
                data["DataPointTooltipOption"]
            )
        )
    if "DataQAEnabledOption" in data:
        import capo_quicksight.types.data_qa_enabled_option

        out["data_qa_enabled_option"] = (
            capo_quicksight.types.data_qa_enabled_option.deserialize_json(
                data["DataQAEnabledOption"]
            )
        )
    if "QuickSuiteActionsOption" in data:
        import capo_quicksight.types.quick_suite_actions_option

        out["quick_suite_actions_option"] = (
            capo_quicksight.types.quick_suite_actions_option.deserialize_json(
                data["QuickSuiteActionsOption"]
            )
        )
    if "ExecutiveSummaryOption" in data:
        import capo_quicksight.types.executive_summary_option

        out["executive_summary_option"] = (
            capo_quicksight.types.executive_summary_option.deserialize_json(
                data["ExecutiveSummaryOption"]
            )
        )
    if "DataStoriesSharingOption" in data:
        import capo_quicksight.types.data_stories_sharing_option

        out["data_stories_sharing_option"] = (
            capo_quicksight.types.data_stories_sharing_option.deserialize_json(
                data["DataStoriesSharingOption"]
            )
        )
    return out
