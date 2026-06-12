"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDataQualityJobDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.data_quality_app_specification
    import aws_sdk_sagemaker.types.data_quality_baseline_config
    import aws_sdk_sagemaker.types.data_quality_job_input
    import aws_sdk_sagemaker.types.monitoring_job_definition_arn
    import aws_sdk_sagemaker.types.monitoring_job_definition_name
    import aws_sdk_sagemaker.types.monitoring_network_config
    import aws_sdk_sagemaker.types.monitoring_output_config
    import aws_sdk_sagemaker.types.monitoring_resources
    import aws_sdk_sagemaker.types.monitoring_stopping_condition
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp


class DescribeDataQualityJobDefinitionResponse(TypedDict):
    job_definition_arn: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_arn.MonitoringJobDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the data quality monitoring job definition.</p>"""
    job_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the data quality monitoring job definition.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the data quality monitoring job definition was created.</p>"""
    data_quality_baseline_config: NotRequired[
        "aws_sdk_sagemaker.types.data_quality_baseline_config.DataQualityBaselineConfig"
    ]
    """<p>The constraints and baselines for the data quality monitoring job definition.</p>"""
    data_quality_app_specification: NotRequired[
        "aws_sdk_sagemaker.types.data_quality_app_specification.DataQualityAppSpecification"
    ]
    """<p>Information about the container that runs the data quality monitoring job.</p>"""
    data_quality_job_input: NotRequired[
        "aws_sdk_sagemaker.types.data_quality_job_input.DataQualityJobInput"
    ]
    """<p>The list of inputs for the data quality monitoring job. Currently endpoints are supported.</p>"""
    data_quality_job_output_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    job_resources: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    network_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_network_config.MonitoringNetworkConfig"
    ]
    """<p>The networking configuration for the data quality monitoring job.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataQualityJobDefinitionResponse) -> dict:
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
    if "data_quality_baseline_config" in value:
        import aws_sdk_sagemaker.types.data_quality_baseline_config

        out["DataQualityBaselineConfig"] = (
            aws_sdk_sagemaker.types.data_quality_baseline_config.serialize_aws_json_1_1(
                value["data_quality_baseline_config"]
            )
        )
    if "data_quality_app_specification" in value:
        import aws_sdk_sagemaker.types.data_quality_app_specification

        out["DataQualityAppSpecification"] = (
            aws_sdk_sagemaker.types.data_quality_app_specification.serialize_aws_json_1_1(
                value["data_quality_app_specification"]
            )
        )
    if "data_quality_job_input" in value:
        import aws_sdk_sagemaker.types.data_quality_job_input

        out["DataQualityJobInput"] = (
            aws_sdk_sagemaker.types.data_quality_job_input.serialize_aws_json_1_1(
                value["data_quality_job_input"]
            )
        )
    if "data_quality_job_output_config" in value:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["DataQualityJobOutputConfig"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["data_quality_job_output_config"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeDataQualityJobDefinitionResponse:
    out: DescribeDataQualityJobDefinitionResponse = {}  # type: ignore[typeddict-item]
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
    if "DataQualityBaselineConfig" in data:
        import aws_sdk_sagemaker.types.data_quality_baseline_config

        out["data_quality_baseline_config"] = (
            aws_sdk_sagemaker.types.data_quality_baseline_config.deserialize_aws_json_1_1(
                data["DataQualityBaselineConfig"]
            )
        )
    if "DataQualityAppSpecification" in data:
        import aws_sdk_sagemaker.types.data_quality_app_specification

        out["data_quality_app_specification"] = (
            aws_sdk_sagemaker.types.data_quality_app_specification.deserialize_aws_json_1_1(
                data["DataQualityAppSpecification"]
            )
        )
    if "DataQualityJobInput" in data:
        import aws_sdk_sagemaker.types.data_quality_job_input

        out["data_quality_job_input"] = (
            aws_sdk_sagemaker.types.data_quality_job_input.deserialize_aws_json_1_1(
                data["DataQualityJobInput"]
            )
        )
    if "DataQualityJobOutputConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["data_quality_job_output_config"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["DataQualityJobOutputConfig"]
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
