"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataQualityBaselineConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_constraints_resource
    import aws_sdk_sagemaker.types.monitoring_statistics_resource
    import aws_sdk_sagemaker.types.processing_job_name


class DataQualityBaselineConfig(TypedDict):
    baselining_job_name: NotRequired[
        "aws_sdk_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the job that performs baselining for the data quality monitoring job.</p>"""
    constraints_resource: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_constraints_resource.MonitoringConstraintsResource"
    ]
    statistics_resource: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_statistics_resource.MonitoringStatisticsResource"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityBaselineConfig) -> dict:
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
    if "statistics_resource" in value:
        import aws_sdk_sagemaker.types.monitoring_statistics_resource

        out["StatisticsResource"] = (
            aws_sdk_sagemaker.types.monitoring_statistics_resource.serialize_aws_json_1_1(
                value["statistics_resource"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityBaselineConfig:
    out: DataQualityBaselineConfig = {}  # type: ignore[typeddict-item]
    if "BaseliningJobName" in data:
        out["baselining_job_name"] = data["BaseliningJobName"]
    if "ConstraintsResource" in data:
        import aws_sdk_sagemaker.types.monitoring_constraints_resource

        out["constraints_resource"] = (
            aws_sdk_sagemaker.types.monitoring_constraints_resource.deserialize_aws_json_1_1(
                data["ConstraintsResource"]
            )
        )
    if "StatisticsResource" in data:
        import aws_sdk_sagemaker.types.monitoring_statistics_resource

        out["statistics_resource"] = (
            aws_sdk_sagemaker.types.monitoring_statistics_resource.deserialize_aws_json_1_1(
                data["StatisticsResource"]
            )
        )
    return out
