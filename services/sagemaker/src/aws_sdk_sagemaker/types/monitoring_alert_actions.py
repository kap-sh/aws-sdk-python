"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertActions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_dashboard_indicator_action


class MonitoringAlertActions(TypedDict):
    model_dashboard_indicator: NotRequired[
        "aws_sdk_sagemaker.types.model_dashboard_indicator_action.ModelDashboardIndicatorAction"
    ]
    """<p>An alert action taken to light up an icon on the Model Dashboard when an alert goes into <code>InAlert</code> status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertActions) -> dict:
    out: dict = {}
    if "model_dashboard_indicator" in value:
        import aws_sdk_sagemaker.types.model_dashboard_indicator_action

        out["ModelDashboardIndicator"] = (
            aws_sdk_sagemaker.types.model_dashboard_indicator_action.serialize_aws_json_1_1(
                value["model_dashboard_indicator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringAlertActions:
    out: MonitoringAlertActions = {}  # type: ignore[typeddict-item]
    if "ModelDashboardIndicator" in data:
        import aws_sdk_sagemaker.types.model_dashboard_indicator_action

        out["model_dashboard_indicator"] = (
            aws_sdk_sagemaker.types.model_dashboard_indicator_action.deserialize_aws_json_1_1(
                data["ModelDashboardIndicator"]
            )
        )
    return out
