"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model
    import aws_sdk_sagemaker.types.model_dashboard_endpoints
    import aws_sdk_sagemaker.types.model_dashboard_model_card
    import aws_sdk_sagemaker.types.model_dashboard_monitoring_schedules
    import aws_sdk_sagemaker.types.transform_job


class ModelDashboardModel(TypedDict, closed=True):
    model: NotRequired["aws_sdk_sagemaker.types.model.Model"]
    """<p>A model displayed in the Model Dashboard.</p>"""
    endpoints: NotRequired[
        "aws_sdk_sagemaker.types.model_dashboard_endpoints.ModelDashboardEndpoints"
    ]
    """<p>The endpoints that host a model.</p>"""
    last_batch_transform_job: NotRequired[
        "aws_sdk_sagemaker.types.transform_job.TransformJob"
    ]
    monitoring_schedules: NotRequired[
        "aws_sdk_sagemaker.types.model_dashboard_monitoring_schedules.ModelDashboardMonitoringSchedules"
    ]
    """<p>The monitoring schedules for a model.</p>"""
    model_card: NotRequired[
        "aws_sdk_sagemaker.types.model_dashboard_model_card.ModelDashboardModelCard"
    ]
    """<p>The model card for a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardModel) -> dict:
    out: dict = {}
    if "model" in value:
        import aws_sdk_sagemaker.types.model

        out["Model"] = aws_sdk_sagemaker.types.model.serialize_aws_json_1_1(
            value["model"]
        )
    if "endpoints" in value:
        import aws_sdk_sagemaker.types.model_dashboard_endpoints

        out["Endpoints"] = (
            aws_sdk_sagemaker.types.model_dashboard_endpoints.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "last_batch_transform_job" in value:
        import aws_sdk_sagemaker.types.transform_job

        out["LastBatchTransformJob"] = (
            aws_sdk_sagemaker.types.transform_job.serialize_aws_json_1_1(
                value["last_batch_transform_job"]
            )
        )
    if "monitoring_schedules" in value:
        import aws_sdk_sagemaker.types.model_dashboard_monitoring_schedules

        out["MonitoringSchedules"] = (
            aws_sdk_sagemaker.types.model_dashboard_monitoring_schedules.serialize_aws_json_1_1(
                value["monitoring_schedules"]
            )
        )
    if "model_card" in value:
        import aws_sdk_sagemaker.types.model_dashboard_model_card

        out["ModelCard"] = (
            aws_sdk_sagemaker.types.model_dashboard_model_card.serialize_aws_json_1_1(
                value["model_card"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDashboardModel:
    out: ModelDashboardModel = {}  # type: ignore[typeddict-item]
    if "Model" in data:
        import aws_sdk_sagemaker.types.model

        out["model"] = aws_sdk_sagemaker.types.model.deserialize_aws_json_1_1(
            data["Model"]
        )
    if "Endpoints" in data:
        import aws_sdk_sagemaker.types.model_dashboard_endpoints

        out["endpoints"] = (
            aws_sdk_sagemaker.types.model_dashboard_endpoints.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if "LastBatchTransformJob" in data:
        import aws_sdk_sagemaker.types.transform_job

        out["last_batch_transform_job"] = (
            aws_sdk_sagemaker.types.transform_job.deserialize_aws_json_1_1(
                data["LastBatchTransformJob"]
            )
        )
    if "MonitoringSchedules" in data:
        import aws_sdk_sagemaker.types.model_dashboard_monitoring_schedules

        out["monitoring_schedules"] = (
            aws_sdk_sagemaker.types.model_dashboard_monitoring_schedules.deserialize_aws_json_1_1(
                data["MonitoringSchedules"]
            )
        )
    if "ModelCard" in data:
        import aws_sdk_sagemaker.types.model_dashboard_model_card

        out["model_card"] = (
            aws_sdk_sagemaker.types.model_dashboard_model_card.deserialize_aws_json_1_1(
                data["ModelCard"]
            )
        )
    return out
