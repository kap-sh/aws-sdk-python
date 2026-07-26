"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelQualityBaselineConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_constraints_resource
    import capo_sagemaker.types.processing_job_name


class ModelQualityBaselineConfig(TypedDict, closed=True):
    baselining_job_name: NotRequired[
        "capo_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the job that performs baselining for the monitoring job.</p>"""
    constraints_resource: NotRequired[
        "capo_sagemaker.types.monitoring_constraints_resource.MonitoringConstraintsResource"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelQualityBaselineConfig) -> dict:
    out: dict = {}
    if "baselining_job_name" in value:
        out["BaseliningJobName"] = value["baselining_job_name"]
    if "constraints_resource" in value:
        import capo_sagemaker.types.monitoring_constraints_resource

        out["ConstraintsResource"] = (
            capo_sagemaker.types.monitoring_constraints_resource.serialize_aws_json_1_1(
                value["constraints_resource"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelQualityBaselineConfig:
    out: ModelQualityBaselineConfig = {}  # type: ignore[typeddict-item]
    if "BaseliningJobName" in data:
        out["baselining_job_name"] = data["BaseliningJobName"]
    if "ConstraintsResource" in data:
        import capo_sagemaker.types.monitoring_constraints_resource

        out["constraints_resource"] = (
            capo_sagemaker.types.monitoring_constraints_resource.deserialize_aws_json_1_1(
                data["ConstraintsResource"]
            )
        )
    return out
