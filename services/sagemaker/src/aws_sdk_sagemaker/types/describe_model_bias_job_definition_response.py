"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelBiasJobDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_bias_app_specification
    import aws_sdk_sagemaker.types.model_bias_baseline_config
    import aws_sdk_sagemaker.types.model_bias_job_input
    import aws_sdk_sagemaker.types.monitoring_job_definition_arn
    import aws_sdk_sagemaker.types.monitoring_job_definition_name
    import aws_sdk_sagemaker.types.monitoring_network_config
    import aws_sdk_sagemaker.types.monitoring_output_config
    import aws_sdk_sagemaker.types.monitoring_resources
    import aws_sdk_sagemaker.types.monitoring_stopping_condition
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp


class DescribeModelBiasJobDefinitionResponse(TypedDict):
    job_definition_arn: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_arn.MonitoringJobDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model bias job.</p>"""
    job_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the bias job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the model bias job was created.</p>"""
    model_bias_baseline_config: NotRequired[
        "aws_sdk_sagemaker.types.model_bias_baseline_config.ModelBiasBaselineConfig"
    ]
    """<p>The baseline configuration for a model bias job.</p>"""
    model_bias_app_specification: NotRequired[
        "aws_sdk_sagemaker.types.model_bias_app_specification.ModelBiasAppSpecification"
    ]
    """<p>Configures the model bias job to run a specified Docker container image.</p>"""
    model_bias_job_input: NotRequired[
        "aws_sdk_sagemaker.types.model_bias_job_input.ModelBiasJobInput"
    ]
    """<p>Inputs for the model bias job.</p>"""
    model_bias_job_output_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    job_resources: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    network_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_network_config.MonitoringNetworkConfig"
    ]
    """<p>Networking options for a model bias job.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelBiasJobDefinitionResponse) -> dict:
    out: dict = {}
    if "job_definition_arn" in value:
        out["JobDefinitionArn"] = value["job_definition_arn"]
    if "job_definition_name" in value:
        out["JobDefinitionName"] = value["job_definition_name"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "model_bias_baseline_config" in value:
        import aws_sdk_sagemaker.types.model_bias_baseline_config

        out["ModelBiasBaselineConfig"] = (
            aws_sdk_sagemaker.types.model_bias_baseline_config.serialize_aws_json_1_1(
                value["model_bias_baseline_config"]
            )
        )
    if "model_bias_app_specification" in value:
        import aws_sdk_sagemaker.types.model_bias_app_specification

        out["ModelBiasAppSpecification"] = (
            aws_sdk_sagemaker.types.model_bias_app_specification.serialize_aws_json_1_1(
                value["model_bias_app_specification"]
            )
        )
    if "model_bias_job_input" in value:
        import aws_sdk_sagemaker.types.model_bias_job_input

        out["ModelBiasJobInput"] = (
            aws_sdk_sagemaker.types.model_bias_job_input.serialize_aws_json_1_1(
                value["model_bias_job_input"]
            )
        )
    if "model_bias_job_output_config" in value:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["ModelBiasJobOutputConfig"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["model_bias_job_output_config"]
            )
        )
    if "job_resources" in value:
        import aws_sdk_sagemaker.types.monitoring_resources

        out["JobResources"] = (
            aws_sdk_sagemaker.types.monitoring_resources.serialize_aws_json_1_1(
                value["job_resources"]
            )
        )
    if "network_config" in value:
        import aws_sdk_sagemaker.types.monitoring_network_config

        out["NetworkConfig"] = (
            aws_sdk_sagemaker.types.monitoring_network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "stopping_condition" in value:
        import aws_sdk_sagemaker.types.monitoring_stopping_condition

        out["StoppingCondition"] = (
            aws_sdk_sagemaker.types.monitoring_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelBiasJobDefinitionResponse:
    out: DescribeModelBiasJobDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "JobDefinitionArn" in data:
        out["job_definition_arn"] = data["JobDefinitionArn"]
    if "JobDefinitionName" in data:
        out["job_definition_name"] = data["JobDefinitionName"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ModelBiasBaselineConfig" in data:
        import aws_sdk_sagemaker.types.model_bias_baseline_config

        out["model_bias_baseline_config"] = (
            aws_sdk_sagemaker.types.model_bias_baseline_config.deserialize_aws_json_1_1(
                data["ModelBiasBaselineConfig"]
            )
        )
    if "ModelBiasAppSpecification" in data:
        import aws_sdk_sagemaker.types.model_bias_app_specification

        out["model_bias_app_specification"] = (
            aws_sdk_sagemaker.types.model_bias_app_specification.deserialize_aws_json_1_1(
                data["ModelBiasAppSpecification"]
            )
        )
    if "ModelBiasJobInput" in data:
        import aws_sdk_sagemaker.types.model_bias_job_input

        out["model_bias_job_input"] = (
            aws_sdk_sagemaker.types.model_bias_job_input.deserialize_aws_json_1_1(
                data["ModelBiasJobInput"]
            )
        )
    if "ModelBiasJobOutputConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["model_bias_job_output_config"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["ModelBiasJobOutputConfig"]
            )
        )
    if "JobResources" in data:
        import aws_sdk_sagemaker.types.monitoring_resources

        out["job_resources"] = (
            aws_sdk_sagemaker.types.monitoring_resources.deserialize_aws_json_1_1(
                data["JobResources"]
            )
        )
    if "NetworkConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_network_config

        out["network_config"] = (
            aws_sdk_sagemaker.types.monitoring_network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "StoppingCondition" in data:
        import aws_sdk_sagemaker.types.monitoring_stopping_condition

        out["stopping_condition"] = (
            aws_sdk_sagemaker.types.monitoring_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    return out
