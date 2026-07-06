"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringJobDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_app_specification
    import aws_sdk_sagemaker.types.monitoring_baseline_config
    import aws_sdk_sagemaker.types.monitoring_environment_map
    import aws_sdk_sagemaker.types.monitoring_inputs
    import aws_sdk_sagemaker.types.monitoring_output_config
    import aws_sdk_sagemaker.types.monitoring_resources
    import aws_sdk_sagemaker.types.monitoring_stopping_condition
    import aws_sdk_sagemaker.types.network_config
    import aws_sdk_sagemaker.types.role_arn


class MonitoringJobDefinition(TypedDict, closed=True):
    baseline_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_baseline_config.MonitoringBaselineConfig"
    ]
    """<p>Baseline configuration used to validate that the data conforms to the specified constraints and statistics</p>"""
    monitoring_inputs: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_inputs.MonitoringInputs"
    ]
    """<p>The array of inputs for the monitoring job. Currently we support monitoring an Amazon SageMaker AI Endpoint.</p>"""
    monitoring_output_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    """<p>The array of outputs from the monitoring job to be uploaded to Amazon S3.</p>"""
    monitoring_resources: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    """<p>Identifies the resources, ML compute instances, and ML storage volumes to deploy for a monitoring job. In distributed processing, you specify more than one instance.</p>"""
    monitoring_app_specification: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_app_specification.MonitoringAppSpecification"
    ]
    """<p>Configures the monitoring job to run a specified Docker container image.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]
    """<p>Specifies a time limit for how long the monitoring job is allowed to run.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_environment_map.MonitoringEnvironmentMap"
    ]
    """<p>Sets the environment variables in the Docker container.</p>"""
    network_config: NotRequired["aws_sdk_sagemaker.types.network_config.NetworkConfig"]
    """<p>Specifies networking options for an monitoring job.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringJobDefinition) -> dict:
    out: dict = {}
    if "baseline_config" in value:
        import aws_sdk_sagemaker.types.monitoring_baseline_config

        out["BaselineConfig"] = (
            aws_sdk_sagemaker.types.monitoring_baseline_config.serialize_aws_json_1_1(
                value["baseline_config"]
            )
        )
    if "monitoring_inputs" in value:
        import aws_sdk_sagemaker.types.monitoring_inputs

        out["MonitoringInputs"] = (
            aws_sdk_sagemaker.types.monitoring_inputs.serialize_aws_json_1_1(
                value["monitoring_inputs"]
            )
        )
    if "monitoring_output_config" in value:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["MonitoringOutputConfig"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["monitoring_output_config"]
            )
        )
    if "monitoring_resources" in value:
        import aws_sdk_sagemaker.types.monitoring_resources

        out["MonitoringResources"] = (
            aws_sdk_sagemaker.types.monitoring_resources.serialize_aws_json_1_1(
                value["monitoring_resources"]
            )
        )
    if "monitoring_app_specification" in value:
        import aws_sdk_sagemaker.types.monitoring_app_specification

        out["MonitoringAppSpecification"] = (
            aws_sdk_sagemaker.types.monitoring_app_specification.serialize_aws_json_1_1(
                value["monitoring_app_specification"]
            )
        )
    if "stopping_condition" in value:
        import aws_sdk_sagemaker.types.monitoring_stopping_condition

        out["StoppingCondition"] = (
            aws_sdk_sagemaker.types.monitoring_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "environment" in value:
        import aws_sdk_sagemaker.types.monitoring_environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.monitoring_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "network_config" in value:
        import aws_sdk_sagemaker.types.network_config

        out["NetworkConfig"] = (
            aws_sdk_sagemaker.types.network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringJobDefinition:
    out: MonitoringJobDefinition = {}  # type: ignore[typeddict-item]
    if "BaselineConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_baseline_config

        out["baseline_config"] = (
            aws_sdk_sagemaker.types.monitoring_baseline_config.deserialize_aws_json_1_1(
                data["BaselineConfig"]
            )
        )
    if "MonitoringInputs" in data:
        import aws_sdk_sagemaker.types.monitoring_inputs

        out["monitoring_inputs"] = (
            aws_sdk_sagemaker.types.monitoring_inputs.deserialize_aws_json_1_1(
                data["MonitoringInputs"]
            )
        )
    if "MonitoringOutputConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["monitoring_output_config"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["MonitoringOutputConfig"]
            )
        )
    if "MonitoringResources" in data:
        import aws_sdk_sagemaker.types.monitoring_resources

        out["monitoring_resources"] = (
            aws_sdk_sagemaker.types.monitoring_resources.deserialize_aws_json_1_1(
                data["MonitoringResources"]
            )
        )
    if "MonitoringAppSpecification" in data:
        import aws_sdk_sagemaker.types.monitoring_app_specification

        out["monitoring_app_specification"] = (
            aws_sdk_sagemaker.types.monitoring_app_specification.deserialize_aws_json_1_1(
                data["MonitoringAppSpecification"]
            )
        )
    if "StoppingCondition" in data:
        import aws_sdk_sagemaker.types.monitoring_stopping_condition

        out["stopping_condition"] = (
            aws_sdk_sagemaker.types.monitoring_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "Environment" in data:
        import aws_sdk_sagemaker.types.monitoring_environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.monitoring_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "NetworkConfig" in data:
        import aws_sdk_sagemaker.types.network_config

        out["network_config"] = (
            aws_sdk_sagemaker.types.network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
