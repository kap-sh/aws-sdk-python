"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelQualityJobDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_quality_app_specification
    import capo_sagemaker.types.model_quality_baseline_config
    import capo_sagemaker.types.model_quality_job_input
    import capo_sagemaker.types.monitoring_job_definition_arn
    import capo_sagemaker.types.monitoring_job_definition_name
    import capo_sagemaker.types.monitoring_network_config
    import capo_sagemaker.types.monitoring_output_config
    import capo_sagemaker.types.monitoring_resources
    import capo_sagemaker.types.monitoring_stopping_condition
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp


class DescribeModelQualityJobDefinitionResponse(TypedDict, closed=True):
    job_definition_arn: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_arn.MonitoringJobDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model quality job.</p>"""
    job_definition_name: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the quality job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the model quality job was created.</p>"""
    model_quality_baseline_config: NotRequired[
        "capo_sagemaker.types.model_quality_baseline_config.ModelQualityBaselineConfig"
    ]
    """<p>The baseline configuration for a model quality job.</p>"""
    model_quality_app_specification: NotRequired[
        "capo_sagemaker.types.model_quality_app_specification.ModelQualityAppSpecification"
    ]
    """<p>Configures the model quality job to run a specified Docker container image.</p>"""
    model_quality_job_input: NotRequired[
        "capo_sagemaker.types.model_quality_job_input.ModelQualityJobInput"
    ]
    """<p>Inputs for the model quality job.</p>"""
    model_quality_job_output_config: NotRequired[
        "capo_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    job_resources: NotRequired[
        "capo_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    network_config: NotRequired[
        "capo_sagemaker.types.monitoring_network_config.MonitoringNetworkConfig"
    ]
    """<p>Networking options for a model quality job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelQualityJobDefinitionResponse) -> dict:
    out: dict = {}
    if "job_definition_arn" in value:
        out["JobDefinitionArn"] = value["job_definition_arn"]
    if "job_definition_name" in value:
        out["JobDefinitionName"] = value["job_definition_name"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "model_quality_baseline_config" in value:
        import capo_sagemaker.types.model_quality_baseline_config

        out["ModelQualityBaselineConfig"] = (
            capo_sagemaker.types.model_quality_baseline_config.serialize_aws_json_1_1(
                value["model_quality_baseline_config"]
            )
        )
    if "model_quality_app_specification" in value:
        import capo_sagemaker.types.model_quality_app_specification

        out["ModelQualityAppSpecification"] = (
            capo_sagemaker.types.model_quality_app_specification.serialize_aws_json_1_1(
                value["model_quality_app_specification"]
            )
        )
    if "model_quality_job_input" in value:
        import capo_sagemaker.types.model_quality_job_input

        out["ModelQualityJobInput"] = (
            capo_sagemaker.types.model_quality_job_input.serialize_aws_json_1_1(
                value["model_quality_job_input"]
            )
        )
    if "model_quality_job_output_config" in value:
        import capo_sagemaker.types.monitoring_output_config

        out["ModelQualityJobOutputConfig"] = (
            capo_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["model_quality_job_output_config"]
            )
        )
    if "job_resources" in value:
        import capo_sagemaker.types.monitoring_resources

        out["JobResources"] = (
            capo_sagemaker.types.monitoring_resources.serialize_aws_json_1_1(
                value["job_resources"]
            )
        )
    if "network_config" in value:
        import capo_sagemaker.types.monitoring_network_config

        out["NetworkConfig"] = (
            capo_sagemaker.types.monitoring_network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "stopping_condition" in value:
        import capo_sagemaker.types.monitoring_stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.monitoring_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelQualityJobDefinitionResponse:
    out: DescribeModelQualityJobDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "JobDefinitionArn" in data:
        out["job_definition_arn"] = data["JobDefinitionArn"]
    if "JobDefinitionName" in data:
        out["job_definition_name"] = data["JobDefinitionName"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "ModelQualityBaselineConfig" in data:
        import capo_sagemaker.types.model_quality_baseline_config

        out["model_quality_baseline_config"] = (
            capo_sagemaker.types.model_quality_baseline_config.deserialize_aws_json_1_1(
                data["ModelQualityBaselineConfig"]
            )
        )
    if "ModelQualityAppSpecification" in data:
        import capo_sagemaker.types.model_quality_app_specification

        out["model_quality_app_specification"] = (
            capo_sagemaker.types.model_quality_app_specification.deserialize_aws_json_1_1(
                data["ModelQualityAppSpecification"]
            )
        )
    if "ModelQualityJobInput" in data:
        import capo_sagemaker.types.model_quality_job_input

        out["model_quality_job_input"] = (
            capo_sagemaker.types.model_quality_job_input.deserialize_aws_json_1_1(
                data["ModelQualityJobInput"]
            )
        )
    if "ModelQualityJobOutputConfig" in data:
        import capo_sagemaker.types.monitoring_output_config

        out["model_quality_job_output_config"] = (
            capo_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["ModelQualityJobOutputConfig"]
            )
        )
    if "JobResources" in data:
        import capo_sagemaker.types.monitoring_resources

        out["job_resources"] = (
            capo_sagemaker.types.monitoring_resources.deserialize_aws_json_1_1(
                data["JobResources"]
            )
        )
    if "NetworkConfig" in data:
        import capo_sagemaker.types.monitoring_network_config

        out["network_config"] = (
            capo_sagemaker.types.monitoring_network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "StoppingCondition" in data:
        import capo_sagemaker.types.monitoring_stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.monitoring_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    return out
