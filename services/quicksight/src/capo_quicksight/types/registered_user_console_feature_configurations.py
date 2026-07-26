"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserConsoleFeatureConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.amazon_q_in_quick_sight_console_configurations
    import capo_quicksight.types.dashboard_customization_summary_configurations
    import capo_quicksight.types.recent_snapshots_configurations
    import capo_quicksight.types.schedules_configurations
    import capo_quicksight.types.shared_view_configurations
    import capo_quicksight.types.state_persistence_configurations
    import capo_quicksight.types.threshold_alerts_configurations


class RegisteredUserConsoleFeatureConfigurations(TypedDict, closed=True):
    state_persistence: NotRequired[
        "capo_quicksight.types.state_persistence_configurations.StatePersistenceConfigurations"
    ]
    """<p>The state persistence configurations of an embedded Amazon Quick Sight console.</p>"""
    shared_view: NotRequired[
        "capo_quicksight.types.shared_view_configurations.SharedViewConfigurations"
    ]
    """<p>The shared view settings of an embedded dashboard.</p>"""
    amazon_q_in_quick_sight: NotRequired[
        "capo_quicksight.types.amazon_q_in_quick_sight_console_configurations.AmazonQInQuickSightConsoleConfigurations"
    ]
    """<p>The Amazon Q configurations of an embedded Amazon Quick Sight console.</p>"""
    schedules: NotRequired[
        "capo_quicksight.types.schedules_configurations.SchedulesConfigurations"
    ]
    """<p>The schedules configuration for an embedded Quick Sight dashboard.</p>"""
    recent_snapshots: NotRequired[
        "capo_quicksight.types.recent_snapshots_configurations.RecentSnapshotsConfigurations"
    ]
    """<p>The recent snapshots configuration for an embedded Quick Sight dashboard.</p>"""
    threshold_alerts: NotRequired[
        "capo_quicksight.types.threshold_alerts_configurations.ThresholdAlertsConfigurations"
    ]
    """<p>The threshold alerts configuration for an embedded Quick Sight dashboard.</p>"""
    dashboard_customization_summary: NotRequired[
        "capo_quicksight.types.dashboard_customization_summary_configurations.DashboardCustomizationSummaryConfigurations"
    ]
    """<p>The dashboard customization summary configuration for an embedded Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserConsoleFeatureConfigurations) -> dict:
    out: dict = {}
    if "state_persistence" in value:
        import capo_quicksight.types.state_persistence_configurations

        out["StatePersistence"] = (
            capo_quicksight.types.state_persistence_configurations.serialize_json(
                value["state_persistence"]
            )
        )
    if "shared_view" in value:
        import capo_quicksight.types.shared_view_configurations

        out["SharedView"] = (
            capo_quicksight.types.shared_view_configurations.serialize_json(
                value["shared_view"]
            )
        )
    if "amazon_q_in_quick_sight" in value:
        import capo_quicksight.types.amazon_q_in_quick_sight_console_configurations

        out["AmazonQInQuickSight"] = (
            capo_quicksight.types.amazon_q_in_quick_sight_console_configurations.serialize_json(
                value["amazon_q_in_quick_sight"]
            )
        )
    if "schedules" in value:
        import capo_quicksight.types.schedules_configurations

        out["Schedules"] = (
            capo_quicksight.types.schedules_configurations.serialize_json(
                value["schedules"]
            )
        )
    if "recent_snapshots" in value:
        import capo_quicksight.types.recent_snapshots_configurations

        out["RecentSnapshots"] = (
            capo_quicksight.types.recent_snapshots_configurations.serialize_json(
                value["recent_snapshots"]
            )
        )
    if "threshold_alerts" in value:
        import capo_quicksight.types.threshold_alerts_configurations

        out["ThresholdAlerts"] = (
            capo_quicksight.types.threshold_alerts_configurations.serialize_json(
                value["threshold_alerts"]
            )
        )
    if "dashboard_customization_summary" in value:
        import capo_quicksight.types.dashboard_customization_summary_configurations

        out["DashboardCustomizationSummary"] = (
            capo_quicksight.types.dashboard_customization_summary_configurations.serialize_json(
                value["dashboard_customization_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisteredUserConsoleFeatureConfigurations:
    out: RegisteredUserConsoleFeatureConfigurations = {}  # type: ignore[typeddict-item]
    if "StatePersistence" in data:
        import capo_quicksight.types.state_persistence_configurations

        out["state_persistence"] = (
            capo_quicksight.types.state_persistence_configurations.deserialize_json(
                data["StatePersistence"]
            )
        )
    if "SharedView" in data:
        import capo_quicksight.types.shared_view_configurations

        out["shared_view"] = (
            capo_quicksight.types.shared_view_configurations.deserialize_json(
                data["SharedView"]
            )
        )
    if "AmazonQInQuickSight" in data:
        import capo_quicksight.types.amazon_q_in_quick_sight_console_configurations

        out["amazon_q_in_quick_sight"] = (
            capo_quicksight.types.amazon_q_in_quick_sight_console_configurations.deserialize_json(
                data["AmazonQInQuickSight"]
            )
        )
    if "Schedules" in data:
        import capo_quicksight.types.schedules_configurations

        out["schedules"] = (
            capo_quicksight.types.schedules_configurations.deserialize_json(
                data["Schedules"]
            )
        )
    if "RecentSnapshots" in data:
        import capo_quicksight.types.recent_snapshots_configurations

        out["recent_snapshots"] = (
            capo_quicksight.types.recent_snapshots_configurations.deserialize_json(
                data["RecentSnapshots"]
            )
        )
    if "ThresholdAlerts" in data:
        import capo_quicksight.types.threshold_alerts_configurations

        out["threshold_alerts"] = (
            capo_quicksight.types.threshold_alerts_configurations.deserialize_json(
                data["ThresholdAlerts"]
            )
        )
    if "DashboardCustomizationSummary" in data:
        import capo_quicksight.types.dashboard_customization_summary_configurations

        out["dashboard_customization_summary"] = (
            capo_quicksight.types.dashboard_customization_summary_configurations.deserialize_json(
                data["DashboardCustomizationSummary"]
            )
        )
    return out
