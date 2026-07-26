"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_dashboard_indicator_action


class MonitoringAlertActions(TypedDict, closed=True):
    model_dashboard_indicator: NotRequired[
        "capo_sagemaker.types.model_dashboard_indicator_action.ModelDashboardIndicatorAction"
    ]
    """<p>An alert action taken to light up an icon on the Model Dashboard when an alert goes into <code>InAlert</code> status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertActions) -> dict:
    out: dict = {}
    if "model_dashboard_indicator" in value:
        import capo_sagemaker.types.model_dashboard_indicator_action

        out["ModelDashboardIndicator"] = (
            capo_sagemaker.types.model_dashboard_indicator_action.serialize_aws_json_1_1(
                value["model_dashboard_indicator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringAlertActions:
    out: MonitoringAlertActions = {}  # type: ignore[typeddict-item]
    if "ModelDashboardIndicator" in data:
        import capo_sagemaker.types.model_dashboard_indicator_action

        out["model_dashboard_indicator"] = (
            capo_sagemaker.types.model_dashboard_indicator_action.deserialize_aws_json_1_1(
                data["ModelDashboardIndicator"]
            )
        )
    return out
