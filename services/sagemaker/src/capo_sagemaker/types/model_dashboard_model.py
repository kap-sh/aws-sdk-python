"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model
    import capo_sagemaker.types.model_dashboard_endpoints
    import capo_sagemaker.types.model_dashboard_model_card
    import capo_sagemaker.types.model_dashboard_monitoring_schedules
    import capo_sagemaker.types.transform_job


class ModelDashboardModel(TypedDict, closed=True):
    model: NotRequired["capo_sagemaker.types.model.Model"]
    """<p>A model displayed in the Model Dashboard.</p>"""
    endpoints: NotRequired[
        "capo_sagemaker.types.model_dashboard_endpoints.ModelDashboardEndpoints"
    ]
    """<p>The endpoints that host a model.</p>"""
    last_batch_transform_job: NotRequired[
        "capo_sagemaker.types.transform_job.TransformJob"
    ]
    monitoring_schedules: NotRequired[
        "capo_sagemaker.types.model_dashboard_monitoring_schedules.ModelDashboardMonitoringSchedules"
    ]
    """<p>The monitoring schedules for a model.</p>"""
    model_card: NotRequired[
        "capo_sagemaker.types.model_dashboard_model_card.ModelDashboardModelCard"
    ]
    """<p>The model card for a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardModel) -> dict:
    out: dict = {}
    if "model" in value:
        import capo_sagemaker.types.model

        out["Model"] = capo_sagemaker.types.model.serialize_aws_json_1_1(value["model"])
    if "endpoints" in value:
        import capo_sagemaker.types.model_dashboard_endpoints

        out["Endpoints"] = (
            capo_sagemaker.types.model_dashboard_endpoints.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "last_batch_transform_job" in value:
        import capo_sagemaker.types.transform_job

        out["LastBatchTransformJob"] = (
            capo_sagemaker.types.transform_job.serialize_aws_json_1_1(
                value["last_batch_transform_job"]
            )
        )
    if "monitoring_schedules" in value:
        import capo_sagemaker.types.model_dashboard_monitoring_schedules

        out["MonitoringSchedules"] = (
            capo_sagemaker.types.model_dashboard_monitoring_schedules.serialize_aws_json_1_1(
                value["monitoring_schedules"]
            )
        )
    if "model_card" in value:
        import capo_sagemaker.types.model_dashboard_model_card

        out["ModelCard"] = (
            capo_sagemaker.types.model_dashboard_model_card.serialize_aws_json_1_1(
                value["model_card"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDashboardModel:
    out: ModelDashboardModel = {}  # type: ignore[typeddict-item]
    if "Model" in data:
        import capo_sagemaker.types.model

        out["model"] = capo_sagemaker.types.model.deserialize_aws_json_1_1(
            data["Model"]
        )
    if "Endpoints" in data:
        import capo_sagemaker.types.model_dashboard_endpoints

        out["endpoints"] = (
            capo_sagemaker.types.model_dashboard_endpoints.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if "LastBatchTransformJob" in data:
        import capo_sagemaker.types.transform_job

        out["last_batch_transform_job"] = (
            capo_sagemaker.types.transform_job.deserialize_aws_json_1_1(
                data["LastBatchTransformJob"]
            )
        )
    if "MonitoringSchedules" in data:
        import capo_sagemaker.types.model_dashboard_monitoring_schedules

        out["monitoring_schedules"] = (
            capo_sagemaker.types.model_dashboard_monitoring_schedules.deserialize_aws_json_1_1(
                data["MonitoringSchedules"]
            )
        )
    if "ModelCard" in data:
        import capo_sagemaker.types.model_dashboard_model_card

        out["model_card"] = (
            capo_sagemaker.types.model_dashboard_model_card.deserialize_aws_json_1_1(
                data["ModelCard"]
            )
        )
    return out
