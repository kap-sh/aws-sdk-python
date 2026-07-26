"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringJobDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_app_specification
    import capo_sagemaker.types.monitoring_baseline_config
    import capo_sagemaker.types.monitoring_environment_map
    import capo_sagemaker.types.monitoring_inputs
    import capo_sagemaker.types.monitoring_output_config
    import capo_sagemaker.types.monitoring_resources
    import capo_sagemaker.types.monitoring_stopping_condition
    import capo_sagemaker.types.network_config
    import capo_sagemaker.types.role_arn


class MonitoringJobDefinition(TypedDict, closed=True):
    baseline_config: NotRequired[
        "capo_sagemaker.types.monitoring_baseline_config.MonitoringBaselineConfig"
    ]
    """<p>Baseline configuration used to validate that the data conforms to the specified constraints and statistics</p>"""
    monitoring_inputs: NotRequired[
        "capo_sagemaker.types.monitoring_inputs.MonitoringInputs"
    ]
    """<p>The array of inputs for the monitoring job. Currently we support monitoring an Amazon SageMaker AI Endpoint.</p>"""
    monitoring_output_config: NotRequired[
        "capo_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    """<p>The array of outputs from the monitoring job to be uploaded to Amazon S3.</p>"""
    monitoring_resources: NotRequired[
        "capo_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    """<p>Identifies the resources, ML compute instances, and ML storage volumes to deploy for a monitoring job. In distributed processing, you specify more than one instance.</p>"""
    monitoring_app_specification: NotRequired[
        "capo_sagemaker.types.monitoring_app_specification.MonitoringAppSpecification"
    ]
    """<p>Configures the monitoring job to run a specified Docker container image.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]
    """<p>Specifies a time limit for how long the monitoring job is allowed to run.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.monitoring_environment_map.MonitoringEnvironmentMap"
    ]
    """<p>Sets the environment variables in the Docker container.</p>"""
    network_config: NotRequired["capo_sagemaker.types.network_config.NetworkConfig"]
    """<p>Specifies networking options for an monitoring job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringJobDefinition) -> dict:
    out: dict = {}
    if "baseline_config" in value:
        import capo_sagemaker.types.monitoring_baseline_config

        out["BaselineConfig"] = (
            capo_sagemaker.types.monitoring_baseline_config.serialize_aws_json_1_1(
                value["baseline_config"]
            )
        )
    if "monitoring_inputs" in value:
        import capo_sagemaker.types.monitoring_inputs

        out["MonitoringInputs"] = (
            capo_sagemaker.types.monitoring_inputs.serialize_aws_json_1_1(
                value["monitoring_inputs"]
            )
        )
    if "monitoring_output_config" in value:
        import capo_sagemaker.types.monitoring_output_config

        out["MonitoringOutputConfig"] = (
            capo_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["monitoring_output_config"]
            )
        )
    if "monitoring_resources" in value:
        import capo_sagemaker.types.monitoring_resources

        out["MonitoringResources"] = (
            capo_sagemaker.types.monitoring_resources.serialize_aws_json_1_1(
                value["monitoring_resources"]
            )
        )
    if "monitoring_app_specification" in value:
        import capo_sagemaker.types.monitoring_app_specification

        out["MonitoringAppSpecification"] = (
            capo_sagemaker.types.monitoring_app_specification.serialize_aws_json_1_1(
                value["monitoring_app_specification"]
            )
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.monitoring_stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.monitoring_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.monitoring_environment_map

        out["Environment"] = (
            capo_sagemaker.types.monitoring_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "network_config" in value:
        import capo_sagemaker.types.network_config

        out["NetworkConfig"] = (
            capo_sagemaker.types.network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringJobDefinition:
    out: MonitoringJobDefinition = {}  # type: ignore[typeddict-item]
    if "BaselineConfig" in data:
        import capo_sagemaker.types.monitoring_baseline_config

        out["baseline_config"] = (
            capo_sagemaker.types.monitoring_baseline_config.deserialize_aws_json_1_1(
                data["BaselineConfig"]
            )
        )
    if "MonitoringInputs" in data:
        import capo_sagemaker.types.monitoring_inputs

        out["monitoring_inputs"] = (
            capo_sagemaker.types.monitoring_inputs.deserialize_aws_json_1_1(
                data["MonitoringInputs"]
            )
        )
    if "MonitoringOutputConfig" in data:
        import capo_sagemaker.types.monitoring_output_config

        out["monitoring_output_config"] = (
            capo_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["MonitoringOutputConfig"]
            )
        )
    if "MonitoringResources" in data:
        import capo_sagemaker.types.monitoring_resources

        out["monitoring_resources"] = (
            capo_sagemaker.types.monitoring_resources.deserialize_aws_json_1_1(
                data["MonitoringResources"]
            )
        )
    if "MonitoringAppSpecification" in data:
        import capo_sagemaker.types.monitoring_app_specification

        out["monitoring_app_specification"] = (
            capo_sagemaker.types.monitoring_app_specification.deserialize_aws_json_1_1(
                data["MonitoringAppSpecification"]
            )
        )
    if "StoppingCondition" in data:
        import capo_sagemaker.types.monitoring_stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.monitoring_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "Environment" in data:
        import capo_sagemaker.types.monitoring_environment_map

        out["environment"] = (
            capo_sagemaker.types.monitoring_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "NetworkConfig" in data:
        import capo_sagemaker.types.network_config

        out["network_config"] = (
            capo_sagemaker.types.network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
