"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserDashboardFeatureConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.amazon_q_in_quick_sight_dashboard_configurations
    import aws_sdk_quicksight.types.bookmarks_configurations
    import aws_sdk_quicksight.types.dashboard_customization_summary_configurations
    import aws_sdk_quicksight.types.recent_snapshots_configurations
    import aws_sdk_quicksight.types.schedules_configurations
    import aws_sdk_quicksight.types.shared_view_configurations
    import aws_sdk_quicksight.types.state_persistence_configurations
    import aws_sdk_quicksight.types.threshold_alerts_configurations


class RegisteredUserDashboardFeatureConfigurations(TypedDict, closed=True):
    state_persistence: NotRequired[
        "aws_sdk_quicksight.types.state_persistence_configurations.StatePersistenceConfigurations"
    ]
    """<p>The state persistence settings of an embedded dashboard.</p>"""
    bookmarks: NotRequired[
        "aws_sdk_quicksight.types.bookmarks_configurations.BookmarksConfigurations"
    ]
    """<p>The bookmarks configuration for an embedded dashboard in Amazon Quick Sight.</p>"""
    shared_view: NotRequired[
        "aws_sdk_quicksight.types.shared_view_configurations.SharedViewConfigurations"
    ]
    """<p>The shared view settings of an embedded dashboard.</p>"""
    amazon_q_in_quick_sight: NotRequired[
        "aws_sdk_quicksight.types.amazon_q_in_quick_sight_dashboard_configurations.AmazonQInQuickSightDashboardConfigurations"
    ]
    """<p>The Amazon Q configurations of an embedded Amazon Quick Sight dashboard.</p>"""
    schedules: NotRequired[
        "aws_sdk_quicksight.types.schedules_configurations.SchedulesConfigurations"
    ]
    """<p>The schedules configuration for an embedded Quick Sight dashboard.</p>"""
    recent_snapshots: NotRequired[
        "aws_sdk_quicksight.types.recent_snapshots_configurations.RecentSnapshotsConfigurations"
    ]
    """<p>The recent snapshots configuration for an Quick Sight embedded dashboard</p>"""
    threshold_alerts: NotRequired[
        "aws_sdk_quicksight.types.threshold_alerts_configurations.ThresholdAlertsConfigurations"
    ]
    """<p>The threshold alerts configuration for an Quick Sight embedded dashboard.</p>"""
    dashboard_customization_summary: NotRequired[
        "aws_sdk_quicksight.types.dashboard_customization_summary_configurations.DashboardCustomizationSummaryConfigurations"
    ]
    """<p>The dashboard customization summary configuration for an embedded Quick Sight dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserDashboardFeatureConfigurations) -> dict:
    out: dict = {}
    if "state_persistence" in value:
        import aws_sdk_quicksight.types.state_persistence_configurations

        out["StatePersistence"] = (
            aws_sdk_quicksight.types.state_persistence_configurations.serialize_json(
                value["state_persistence"]
            )
        )
    if "bookmarks" in value:
        import aws_sdk_quicksight.types.bookmarks_configurations

        out["Bookmarks"] = (
            aws_sdk_quicksight.types.bookmarks_configurations.serialize_json(
                value["bookmarks"]
            )
        )
    if "shared_view" in value:
        import aws_sdk_quicksight.types.shared_view_configurations

        out["SharedView"] = (
            aws_sdk_quicksight.types.shared_view_configurations.serialize_json(
                value["shared_view"]
            )
        )
    if "amazon_q_in_quick_sight" in value:
        import aws_sdk_quicksight.types.amazon_q_in_quick_sight_dashboard_configurations

        out["AmazonQInQuickSight"] = (
            aws_sdk_quicksight.types.amazon_q_in_quick_sight_dashboard_configurations.serialize_json(
                value["amazon_q_in_quick_sight"]
            )
        )
    if "schedules" in value:
        import aws_sdk_quicksight.types.schedules_configurations

        out["Schedules"] = (
            aws_sdk_quicksight.types.schedules_configurations.serialize_json(
                value["schedules"]
            )
        )
    if "recent_snapshots" in value:
        import aws_sdk_quicksight.types.recent_snapshots_configurations

        out["RecentSnapshots"] = (
            aws_sdk_quicksight.types.recent_snapshots_configurations.serialize_json(
                value["recent_snapshots"]
            )
        )
    if "threshold_alerts" in value:
        import aws_sdk_quicksight.types.threshold_alerts_configurations

        out["ThresholdAlerts"] = (
            aws_sdk_quicksight.types.threshold_alerts_configurations.serialize_json(
                value["threshold_alerts"]
            )
        )
    if "dashboard_customization_summary" in value:
        import aws_sdk_quicksight.types.dashboard_customization_summary_configurations

        out["DashboardCustomizationSummary"] = (
            aws_sdk_quicksight.types.dashboard_customization_summary_configurations.serialize_json(
                value["dashboard_customization_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisteredUserDashboardFeatureConfigurations:
    out: RegisteredUserDashboardFeatureConfigurations = {}  # type: ignore[typeddict-item]
    if "StatePersistence" in data:
        import aws_sdk_quicksight.types.state_persistence_configurations

        out["state_persistence"] = (
            aws_sdk_quicksight.types.state_persistence_configurations.deserialize_json(
                data["StatePersistence"]
            )
        )
    if "Bookmarks" in data:
        import aws_sdk_quicksight.types.bookmarks_configurations

        out["bookmarks"] = (
            aws_sdk_quicksight.types.bookmarks_configurations.deserialize_json(
                data["Bookmarks"]
            )
        )
    if "SharedView" in data:
        import aws_sdk_quicksight.types.shared_view_configurations

        out["shared_view"] = (
            aws_sdk_quicksight.types.shared_view_configurations.deserialize_json(
                data["SharedView"]
            )
        )
    if "AmazonQInQuickSight" in data:
        import aws_sdk_quicksight.types.amazon_q_in_quick_sight_dashboard_configurations

        out["amazon_q_in_quick_sight"] = (
            aws_sdk_quicksight.types.amazon_q_in_quick_sight_dashboard_configurations.deserialize_json(
                data["AmazonQInQuickSight"]
            )
        )
    if "Schedules" in data:
        import aws_sdk_quicksight.types.schedules_configurations

        out["schedules"] = (
            aws_sdk_quicksight.types.schedules_configurations.deserialize_json(
                data["Schedules"]
            )
        )
    if "RecentSnapshots" in data:
        import aws_sdk_quicksight.types.recent_snapshots_configurations

        out["recent_snapshots"] = (
            aws_sdk_quicksight.types.recent_snapshots_configurations.deserialize_json(
                data["RecentSnapshots"]
            )
        )
    if "ThresholdAlerts" in data:
        import aws_sdk_quicksight.types.threshold_alerts_configurations

        out["threshold_alerts"] = (
            aws_sdk_quicksight.types.threshold_alerts_configurations.deserialize_json(
                data["ThresholdAlerts"]
            )
        )
    if "DashboardCustomizationSummary" in data:
        import aws_sdk_quicksight.types.dashboard_customization_summary_configurations

        out["dashboard_customization_summary"] = (
            aws_sdk_quicksight.types.dashboard_customization_summary_configurations.deserialize_json(
                data["DashboardCustomizationSummary"]
            )
        )
    return out
