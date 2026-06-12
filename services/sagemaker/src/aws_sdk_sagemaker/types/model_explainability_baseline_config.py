"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelExplainabilityBaselineConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_constraints_resource
    import aws_sdk_sagemaker.types.processing_job_name


class ModelExplainabilityBaselineConfig(TypedDict):
    baselining_job_name: NotRequired[
        "aws_sdk_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the baseline model explainability job.</p>"""
    constraints_resource: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_constraints_resource.MonitoringConstraintsResource"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelExplainabilityBaselineConfig) -> dict:
    out: dict = {}
    if "baselining_job_name" in value:
        out["BaseliningJobName"] = value["baselining_job_name"]
    if "constraints_resource" in value:
        import aws_sdk_sagemaker.types.monitoring_constraints_resource

        out["ConstraintsResource"] = (
            aws_sdk_sagemaker.types.monitoring_constraints_resource.serialize_aws_json_1_1(
                value["constraints_resource"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelExplainabilityBaselineConfig:
    out: ModelExplainabilityBaselineConfig = {}  # type: ignore[typeddict-item]
    if "BaseliningJobName" in data:
        out["baselining_job_name"] = data["BaseliningJobName"]
    if "ConstraintsResource" in data:
        import aws_sdk_sagemaker.types.monitoring_constraints_resource

        out["constraints_resource"] = (
            aws_sdk_sagemaker.types.monitoring_constraints_resource.deserialize_aws_json_1_1(
                data["ConstraintsResource"]
            )
        )
    return out
